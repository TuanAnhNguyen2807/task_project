from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):
    def test_task_creation(self):
        t = Task.objects.create(title="t1", description="desc")
        self.assertEqual(str(t), "t1")
