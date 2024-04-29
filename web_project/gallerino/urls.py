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
    path('gallery/<int:gallery_id>/', display_images, name = 'display_images'),
    path('image_upload/<int:gallery_id>/', image_upload, name = 'image_upload'),
    path('gallery_success/<int:gallery_id>', gallery_success, name = 'gallery_success'),
    path('success/<int:gallery_id>', success, name = 'success'),
    path('delete/<int:image_id>/', delete_image, name='delete_image'),

]