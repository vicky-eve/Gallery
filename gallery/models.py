from django.db import models


# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls, id, name):
        cls.objects.filter(id=id).update(name=name)

class Location(models.Model):
    name=models.CharField(max_length=100)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls, id, name):
        cls.objects.filter(id=id).update(name=name)

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

    @classmethod
    def update_image(cls, id, name,details,category, location ):
        cls.objects.filter(id=id).update(name=name, details=details, category=category, location=location)

    @classmethod
    def get_image(cls):
        photo = Image.object()
        return photo

    @classmethod
    def search_image(cls,search_category):
        photo = cls.objects.filter(category__name__icontains=search_category)
        return photo

    @classmethod
    def filter_by_location(cls, filter_location):
        location = cls.objects.filter(location__name=filter_location).all()
        return location

    def __str__(self) -> str:
        return self.name
