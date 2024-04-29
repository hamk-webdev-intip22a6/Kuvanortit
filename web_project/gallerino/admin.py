from django.contrib import admin
from .models import Post, Gallery

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('description', 'image', 'gallery', 'pub_date', 'mod_date')
    search_fields = ['description']
    list_filter = ['pub_date', 'mod_date']

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'thumbnail', 'pub_date', 'mod_date')
    search_fields = ['description']
    list_filter = ['pub_date', 'mod_date']

admin.site.register(Post, PostAdmin)
admin.site.register(Gallery, GalleryAdmin)