
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Gallery
from .forms import UploadForm, GalleryForm
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from PIL import Image, ImageSequence
from django.conf import settings
from django.core.files.base import ContentFile
import os
from io import BytesIO




@login_required
def display_galleries(request):
    if request.method == "GET":
        galleries = Gallery.objects.filter(user = request.user)
        return render(request, 'gallerino/index.html', {'galleries': galleries})


@login_required
def display_images(request, gallery_id):
    if request.method == "GET":
        gallery = get_object_or_404(Gallery, pk=gallery_id)
        posts = Post.objects.filter(gallery = gallery)
        return render(request, 'gallerino/gallery.html', {'posts': posts, 'gallery': gallery})



from PIL import Image, ImageSequence

def resize_image(image_file, size=(500, 500), quality=95):
    with Image.open(image_file) as image:
        if image.format == 'PNG':
            rgba_image = image.convert('RGBA')
            background = Image.new('RGBA', rgba_image.size, (255, 255, 255))
            resized_image = Image.alpha_composite(background, rgba_image)
            resized_image = resized_image.resize(size)
            resized_image = resized_image.convert('RGB')
        elif image.format == 'GIF':
            frames = []
            for frame in ImageSequence.Iterator(image):
                resized_frame = frame.resize(size)
                resized_frame = resized_frame.convert('RGB')  # Convert GIF frames to RGB
                frames.append(resized_frame)
            resized_image = frames[0] if len(frames) == 1 else frames
        else:
            resized_image = image.resize(size)
            if resized_image.mode != 'RGB':
                resized_image = resized_image.convert('RGB')

        resized_image_io = BytesIO()
        if image.format == 'GIF':
            resized_image[0].save(resized_image_io, format='GIF', save_all=True, append_images=resized_image[1:], quality=quality)
        elif image.format == 'PNG':
            resized_image.save(resized_image_io, format='PNG', optimize=True, quality=quality)
        else:
            resized_image.save(resized_image_io, format='JPEG', quality=quality)

        resized_image_io.seek(0)
        resized_image_content = ContentFile(resized_image_io.getvalue())
        resized_image_content.name = image_file.name
        return resized_image_content




@login_required
def create_gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            gallery = form.save(commit = False)

            if 'thumbnail' in request.FILES:
                thumbnail_file = request.FILES['thumbnail']
                resized_thumbnail = resize_image(thumbnail_file, size=(500, 500), quality=100)
                gallery.thumbnail = resized_thumbnail
            else:
                # Set default thumbnail
                default_thumbnail_path = os.path.join(settings.MEDIA_ROOT, 'gallerino_thumbnail_placeholder.png')
                with open(default_thumbnail_path, 'rb') as f:
                    default_thumbnail_content = f.read()
                default_thumbnail = ContentFile(default_thumbnail_content)
                gallery.thumbnail.save('default_thumbnail.jpg', default_thumbnail)
            gallery.save()
            return redirect('gallerino:gallery_success', gallery_id=gallery.pk)
    else:
        form = GalleryForm()
    return render(request, 'gallerino/gallery_creation.html', {'form': form})




@login_required
def image_upload(request, gallery_id):
    gallery = get_object_or_404(Gallery, pk=gallery_id)
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.gallery = gallery
            if 'image' in request.FILES:
                image_file = request.FILES['image']
                resized_image = resize_image(image_file)
                post.image = resized_image
            post.save()
            if gallery.placeholder and gallery.post_set.exists():

                first_image = gallery.post_set.order_by('id').first()
                if first_image:
                    gallery.thumbnail = first_image.image
                    gallery.save()
            return redirect(reverse('gallerino:success', kwargs={'gallery_id' : gallery_id}))
    else:
        form = UploadForm()
    return render(request, 'gallerino/upload.html', {'form': form, 'gallery': gallery})




@login_required
def gallery_success(request, gallery_id):
    gallery = get_object_or_404(Gallery, pk=gallery_id)
    return render(request, 'gallerino/gallery_success.html', {'gallery': gallery})



@login_required
def success(request, gallery_id):
    gallery = get_object_or_404(Gallery, pk=gallery_id)
    return render(request, 'gallerino/success.html', {'gallery': gallery})
   
   
