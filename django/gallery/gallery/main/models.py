from django.db import models

# Create your models here.
class GalleryModel(models.Model):
    image = models.ImageField(upload_to='my_images')
    date = models.DateTimeField(auto_now_add=True)
