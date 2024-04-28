from django import forms
from .models import Post, Gallery



class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = {'title' ,'description', 'thumbnail'}

    def __init__(self, *args, **kwargs):
        super(GalleryForm, self).__init__(*args, **kwargs)
        self.fields['thumbnail'].required = False

class UploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description', 'image']

