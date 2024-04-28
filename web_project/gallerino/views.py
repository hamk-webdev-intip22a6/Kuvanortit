from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponse
from .models import Post
from .forms import UploadForm
# Create your views here.



# def index(request):
#     return render(request, "gallerino/index.html")



def display_images(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, 'gallerino/index.html', {'posts' : posts})
    
def image_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallerino:success')
    else:
        form = UploadForm()
    return render(request, 'gallerino/upload.html', {'form' : form})



def success(request):
    return render(request, 'gallerino/success.html', {})