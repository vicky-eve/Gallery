from django.db import models


# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)

class Location(models.Model):
    name=models.CharField(max_length=100)

class Image(models.Model):
    photo=models.ImageField(upload_to=('images/'))
    date_posted=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=100)
    details=models.TextField(max_length=1000)
    category=models.ForeignKey(Category)
    location=models.ForeignKey(Location)
    
    def save_photo(self):
        self.save()
