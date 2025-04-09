from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title='Test Title',
            body='Test Body'
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.title, 'Test Title')
        self.assertEqual(self.post.body, 'Test Body')
        self.assertEqual(str(self.post), 'Test Title')
