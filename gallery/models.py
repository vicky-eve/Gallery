from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Image(models.Model):
    photo=CloudinaryField('Image')
    name=models.CharField(max_length=100)
    details=models.TextField(max_length=1000)
    
    def __str__(self):
        return self.first_name