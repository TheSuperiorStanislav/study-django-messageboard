from django.test import TestCase
from django.urls import reverse
from.models import Post

# Create your tests here.
class PostModelTest(TestCase):
    test_str = 'just a test'

    def setUp(self):
        Post.objects.create(text = self.test_str)

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, self.test_str)
    
class HomePageViewTest(TestCase):

    test_str = 'just a test'

    def setUp(self):
        Post.objects.create(text = self.test_str)
    
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code,200)
    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
    
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,'home.html')
        