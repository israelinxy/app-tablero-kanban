from django.test import TestCase
from django.contrib.auth.models import User
from projects.models import Project
from .models import Column, Task

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.project = Project.objects.create(name='Test Project', owner=self.user)
        self.column = Column.objects.create(title='To Do', project=self.project)
        self.task = Task.objects.create(title='Test Task', column=self.column)

    def test_task_creation(self):
        self.assertTrue(isinstance(self.task, Task))
        self.assertEqual(self.task.__str__(), self.task.title)

class TaskAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.project = Project.objects.create(name='Test Project', owner=self.user)
        self.column = Column.objects.create(title='To Do', project=self.project)

    def test_create_task(self):
        data = {
            'title': 'New Task',
            'column': self.column.id
        }
        response = self.client.post('/api/tasks/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Task.objects.count(), 1)  # Asegúrate de que se ha creado una nueva tarea

    def test_get_tasks_by_project(self):
        response = self.client.get(f'/api/tasks/by_project/?project_id={self.project.id}')
        self.assertEqual(response.status_code, 200)
