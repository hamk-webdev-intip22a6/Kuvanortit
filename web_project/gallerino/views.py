from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponse
from .models import Post, Gallery
from .forms import UploadForm, GalleryForm
# Create your views here.



# def index(request):
#     return render(request, "gallerino/index.html")



def display_galleries(request):
    if request.method == "GET":
        galleries = Gallery.objects.all()
        return render(request, 'gallerino/index.html', {'galleries' : galleries})


def display_images(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, 'gallerino/gallery.html', {'posts' : posts})
    


def create_gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallerino:gallery_success')
    else:
        form = GalleryForm()
    return render(request, 'gallerino/gallery_creation.html', {'form' : form})



def image_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallerino:success')
    else:
        form = UploadForm()
    return render(request, 'gallerino/upload.html', {'form' : form})


def gallery_success(request):
    return render(request, 'gallerino/gallery_success.html')


def success(request):
    return render(request, 'gallerino/success.html', {})