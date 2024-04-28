from django.db import models

# Create your models here.

class Post(models.Model):

    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published', auto_now_add=True)
    mod_date = models.DateTimeField('Date modified', auto_now=True)