from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Project

class ProjectModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.project = Project.objects.create(
            name='Test Project',
            description='Test Description',
            owner=self.user
        )

    def test_project_creation(self):
        self.assertTrue(isinstance(self.project, Project))
        self.assertEqual(self.project.__str__(), self.project.name)

class ProjectAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_project(self):
        data = {
            'name': 'New Project',
            'description': 'New Description'
        }
        response = self.client.post('/api/projects/', data)
        self.assertEqual(response.status_code, 201)

    def test_my_projects(self):
        response = self.client.get('/api/projects/my_projects/')
        self.assertEqual(response.status_code, 200)