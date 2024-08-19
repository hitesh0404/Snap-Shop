from django.test import TestCase
from django.utils.html import strip_tags
from account.models import Carousel

class CarouselModelTest(TestCase):

    def setUp(self):
        self.carousel = Carousel.objects.create(
            image='carousel/sample_image.jpg',
            title='<h1>Sample Title</h1>',
            description='<p>This is a sample description.</p>')
        self.carousel.save()

    def test_carousel_creation(self):

        """Test if the Carousel instance is created correctly"""
        self.assertEqual(self.carousel.image.name, 'carousel/sample_image.jpg')
        self.assertEqual(self.carousel.title, '<h1>Sample Title</h1>')
        self.assertEqual(self.carousel.description, '<p>This is a sample description.</p>')
    
    def test_carousel_str_method(self):

        """Test the __str__ method of the Carousel model"""
        expected_str = strip_tags(self.carousel.title)
        self.assertEqual(str(self.carousel), expected_str)
        
    def test_carousel_default_image(self):

        """Test if the default image is set correctly"""
        default_carousel = Carousel.objects.create(
            title='<h1>Default Title</h1>',
            description='<p>This is a default description.</p>')
        self.assertEqual(default_carousel.image.name, 'media\\banner-01.jpg')
