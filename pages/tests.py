from django.test import TestCase
from django.urls import reverse
from.models import Blog

# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        self.blog = Blog.objects.create(
           title = 'testing',
           author = 'afc' ,
           text = 'model testing'
        )

    def test_string_represantation(self):
        blog = Blog(title='sample title')
        self.assertEqual(str(blog), blog.title)

    def test_content(self):
        self.assertEqual(f'{self.blog.title}', 'testing')
        self.assertEqual(f'{self.blog.author}', 'afc')
        self.assertEqual(f'{self.blog.text}', 'model testing')

    def test_blog_list_view(self):
        response = self.client.get(reverse('pages:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testing')
        self.assertTemplateUsed(response, 'pages/index.html')

    def test_page_view(self):
        response = self.client.get(reverse())