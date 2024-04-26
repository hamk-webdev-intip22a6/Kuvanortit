from django.shortcuts import render, get_object_or_404
from django.views import generic
# Create your views here.

def index(request):
    return render(request, "gallerino/index.html")