# from django.shortcuts import render, get_object_or_404, redirect
# from django.views import generic
# from django.http import HttpResponse
# from .models import Post, Gallery
# from .forms import UploadForm, GalleryForm
# # Create your views here.



# # def index(request):
# #     return render(request, "gallerino/index.html")



# def display_galleries(request):
#     if request.method == "GET":
#         galleries = Gallery.objects.all()
#         return render(request, 'gallerino/index.html', {'galleries' : galleries})


# def display_images(request, gallery_id):
#     if request.method == "GET":
#         posts = Post.objects.all()
#         gallery = get_object_or_404(Gallery, pk=gallery_id)
#         return render(request, 'gallerino/gallery.html', {'posts' : posts, 'gallery' : gallery})
    


# def create_gallery(request, gallery_id):
#     if request.method == 'POST':
#         form = GalleryForm(request.POST, request.FILES)
#         if form.is_valid():
#             gallery = form.save()
#             return redirect('gallerino:gallery_success', pk=gallery_id)
#     else:
#         form = GalleryForm()
#     return render(request, 'gallerino/gallery_creation.html', {'form' : form})



# def image_upload(request, gallery_id):
#     gallery = get_object_or_404(Gallery, pk=gallery_id)
#     if request.method == 'POST':
#         form = UploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.gallery = gallery
#             post.save()
#             return redirect('gallerino:success')
#     else:
#         form = UploadForm()
#     return render(request, 'gallerino/upload.html', {'form' : form})


# def gallery_success(request, pk):
#     gallery = Gallery.objects.get(pk=pk)
#     return render(request, 'gallerino/gallery_success.html', {'gallery' : gallery})


# def success(request):
#     return render(request, 'gallerino/success.html', {})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Gallery
from .forms import UploadForm, GalleryForm
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



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


@login_required
def create_gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            gallery = form.save()
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
            post.save()
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
   
   
    # gallery_id = request.session.get('gallery_id')
    # if gallery_id:

    # else:
    #     # Handle the case where gallery_id is not found in the session
    #     # For example, you can redirect the user to another page or display an error message
    #     return HttpResponse("Gallery ID not found in session.")

