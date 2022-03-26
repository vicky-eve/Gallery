from django.db import models


# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)

class Location(models.Model):
    name=models.CharField(max_length=100)

class Image(models.Model):
    photo=models.ImageField(upload_to=('images/'),null=True)
    date_posted=models.DateTimeField(auto_now_add=True,null=True)
    name=models.CharField(max_length=100)
    details=models.TextField(max_length=1000)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    location=models.ForeignKey(Location,on_delete=models.CASCADE,null=True)
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update()

    @classmethod
    def get_image(cls):
        photo = Image.object()
        return photo

    @classmethod
    def search_image(cls,search_category):
        photo = cls.objects.filter(category__name__icontains=search_category)
        return photo



    def __str__(self) -> str:
        return self.name
