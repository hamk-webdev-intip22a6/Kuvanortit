from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Gallery (models.Model):

    title = models.CharField(max_length=60, default='My Gallery')
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    thumbnail = models.ImageField(upload_to='images/', default='gallerino_thumbnail_placeholder.png')
    pub_date = models.DateTimeField('Date published', auto_now_add=True)
    mod_date = models.DateTimeField('Date modified', auto_now=True)
    


class Post(models.Model):

    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, default=1)       #Tän vois muuttaa ettei saa olla null mut nyt on myöhä ja aivot sulaa
    pub_date = models.DateTimeField('Date published', auto_now_add=True)
    mod_date = models.DateTimeField('Date modified', auto_now=True)

