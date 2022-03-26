from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        """ 
        create an image instance
        """
        self.category=Category(name='House facilities')
        self.category.save_category

        self.location=Location(name='Roysambu')
        self.location.save_location

        self.image = Image(name= 'Wardrobe', photo= 'wardrobe.png', details= 'the beauty of a bedroom is in the location and design of the wardrobe', location=self.location, category=self.category)
        self.image.save_image

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

   

    def test_save_image(self):
        self.image.save_image
        images = Image.objects.all()
        self.assertTrue(len(images)>0)
    
    def test_delete_image(self):
        image=Image.objects.filter(name='imagetest')
        image.delete()
        self.assertTrue(len(Image.objects.all())==0)

    def test_update_image(self):
        new_photo='Wallunit.png'
        self.image.update_image(self.image.id,new_photo)
        new_photo=Image.objects.filter(photo='Wallunit.png')
        self.assertTrue(len(new_photo)==1)

    def test_get_image(self):
        image_search=self.image.get_image(self.image.id)
        image = Image.objects.filter(id=self.image.id)
        self.assertTrue(image_search,image)

    def test_search_by_category(self):
        category_search=self.image.search_image('House facilities')
        self.assertTrue(len(category_search)>=1)

    def test_filter_by_location(self):
        location_search=self.image.filter_by_location('Roysambu')
        self.assertTrue(len(location_search)==1)

class LocationTestClass(TestCase):

    def setUp(self):
        self.location=Location(name='Roysambu')
        self.location.save_location

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def test_save_location(self):
        self.location.save_location()
        location=Location.objects.all()
        self.assertTrue(len(location)>0)

    def test_delete_location(self):
        self.location.delete_location()
        location=Location.objects.all()
        self.assertTrue(len(location)==0)

    def test_update_location(self):
        new_location='Juja'
        self.location.update_location(self.location.id,new_location)
        new_location=Image.objects.filter(location='Juja')
        self.assertTrue(len(new_location)==1)
    
class CategoryTestClass(TestCase):

    def setUp(self):
        self.category=Category(name='House facilities')
        self.category.save_category

    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    def test_save_category(self):
        self.category.save_category()
        category=Category.objects.all()
        self.assertTrue(len(category)>0)

    def test_delete_category(self):
        self.category.delete_category()
        category=Category.objects.all()
        self.assertTrue(len(category)==0)

    def test_update_category(self):
        new_category='Bags'
        self.category.update_category(self.category.id,new_category)
        new_category=Image.objects.filter(photo='Bags')
        self.assertTrue(len(new_category)==1)

