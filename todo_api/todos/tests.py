from django.test import TestCase
from django.urls import reverse
from django.test import TestCase

from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title="First Todo",
            body="A body of text here"
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "First Todo")
        self.assertEqual(self.todo.body, "A body of text here")
        self.assertEqual(str(self.todo), "First Todo")

    def test_api_list_view(self):
        response = self.client.get(reverse('todo-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_api_detail_view(self):
        response = self.client.get(
            reverse('todo-detail', kwargs={'pk': self.todo.id}),
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)
