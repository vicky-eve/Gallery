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
    
    

