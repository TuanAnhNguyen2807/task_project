from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Task

class TaskModelTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_task_creation(self):
        task = Task.objects.create(
            title="Test Task",
            description="This is a test task.",
            user=self.user
        )
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "This is a test task.")
        self.assertFalse(task.is_completed)
        self.assertEqual(task.user.username, "testuser")

    def test_task_str_method(self):
        task = Task.objects.create(
            title="Another Task",
            user=self.user
        )
        self.assertEqual(str(task), "Another Task")

    def test_default_values(self):
        task = Task.objects.create(
            title="Default Task",
            user=self.user
        )
        # is_completed should default to False
        self.assertFalse(task.is_completed)
