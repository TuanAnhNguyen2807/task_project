from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from ..models import Task
from rest_framework_simplejwt.tokens import RefreshToken

class TaskViewSetTest(APITestCase):

    def setUp(self):
        # Create two users
        self.user1 = User.objects.create_user(username='user1', password='pass123')
        self.user2 = User.objects.create_user(username='user2', password='pass123')

        # Create tasks for user1
        self.task1 = Task.objects.create(title="Task 1", user=self.user1)
        self.task2 = Task.objects.create(title="Task 2", is_completed=True, user=self.user1)

        # Create a task for user2
        self.task3 = Task.objects.create(title="Task 3", user=self.user2)

        # Login as user1
        refresh = RefreshToken.for_user(self.user1)
        access_token = str(refresh.access_token)
        self.client.cookies['access'] = access_token

        # URL for tasks list (assuming router uses 'tasks' as basename)
        self.list_url = reverse('task-list')

    def test_list_tasks_only_user_tasks(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        # Only user1's tasks should be returned
        self.assertEqual(len(response.data['results']), 2)
        titles = [task['title'] for task in response.data['results']]
        self.assertIn('Task 1', titles)
        self.assertIn('Task 2', titles)
        self.assertNotIn('Task 3', titles)

    def test_create_task(self):
        data = {"title": "New Task"}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.filter(user=self.user1, title="New Task").count(), 1)

    def test_filter_is_completed(self):
        response = self.client.get(self.list_url, {'is_completed': True})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Task 2')

    def test_ordering(self):
        response = self.client.get(self.list_url, {'ordering': 'created_at'})
        self.assertEqual(response.status_code, 200)
        # The first task should be task1 (earliest created)
        self.assertEqual(response.data['results'][0]['title'], 'Task 1')

    def test_search(self):
        response = self.client.get(self.list_url, {'q': 'Task 1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Task 1')
