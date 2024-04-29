
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Gallery
from .forms import UploadForm, GalleryForm
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from PIL import Image
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




def resize_image(image_file, size=(500, 500), quality=95):
    """
    Resize the uploaded image to the specified size and quality.
    """
    # Open the image file
    with Image.open(image_file) as image:
        # Resize the image
        resized_image = image.resize(size)
        # Convert the image to RGB mode if it's not already
        if resized_image.mode != 'RGB':
            resized_image = resized_image.convert('RGB')
        # Create a BytesIO object to store the resized image data
        resized_image_io = BytesIO()
        # Save the resized image to the BytesIO object with the specified quality
        resized_image.save(resized_image_io, format='JPEG', quality=quality)
        # Seek to the beginning of the BytesIO object
        resized_image_io.seek(0)
        # Create a ContentFile object containing the resized image data
        resized_image_content = ContentFile(resized_image_io.getvalue())
        # Set the ContentFile object's name attribute to the original image's name
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
                resized_thumbnail = resize_image(thumbnail_file, size=(50, 50), quality=100)
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
   
   
