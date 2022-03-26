from django.db import models


# Create your models here.

class Image(models.Model):
    image=models.ImageField(upload_to=('images/'))
    date_posted=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=100)
    details=models.TextField(max_length=1000)
    
    def save_photo(self):
        self.save()