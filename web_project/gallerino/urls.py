from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "gallerino"
urlpatterns = [
    # path("", views.index, name="index")
    path('', display_galleries, name = 'display_galleries'),
    path('create', create_gallery, name = 'create_gallery' ),
    # path('gallery', display_images, name = 'display_images'),
    path('gallery/<int:pk>/', display_images, name = 'display_images'),
    path('image_upload', image_upload, name = 'image_upload'),
    path('gallery_success', gallery_success, name = 'gallery_success'),
    path('success', success, name = 'success'),

]