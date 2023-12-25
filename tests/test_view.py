from rest_framework.test import APITestCase
from Api.models import Task
from rest_framework import status


class TaskViewTest(APITestCase):
    def test_tasks_list(self):
        response = self.client.get('/taskapi/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tasks_get_single_data(self):
        Task.objects.create(title="Task Name", desc="Description", due_date="2023-12-28", tags="a,b", status="OPEN")
        response = self.client.get('/taskapi/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_create_success(self):
        data = {
            'title': "Task Name",
            'desc': "Description",
            'due_date': "2023-12-28",
            'tags': "a,b",
            'status': "OPEN"
        }
        response = self.client.post('/taskapi/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['msg'], "Task Created")

    def test_task_create_fail(self):
        data = {
            'title': "Task Name",
            'desc': "Description",
            'due_date': "2023-12-16",
            'tags': "a,b",
            'status': "OPEN"
        }
        response = self.client.post('/taskapi/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_task_update_success(self):
        Task.objects.create(title="Task Name", desc="Description", due_date="2023-12-24", tags="a,b", status="OPEN")

        data = {
            'title': "Task 2",
            'desc': "Description 2",
            'due_date': "2023-12-28",
            'tags': "tag2,tag3",
            'status': "WORKING"
        }
        response = self.client.put('/taskapi/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.data['msg'], "Task Updated")

    def test_task_update_fail(self):
        Task.objects.create(title="Task Name", desc="Description", due_date="2023-12-24", tags="a,b", status="OPEN")

        data = {
            'title': "Task 2",
            'desc': "Description 2",
            'due_date': "2023-12-16",
            'tags': "tag2,tag3",
            'status': "WORKING"
        }
        response = self.client.put('/taskapi/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_task_update_partially_success(self):
        Task.objects.create(title="Task Name", desc="Description", due_date="2023-12-28", tags="a,b", status="OPEN")

        data = {
            'title': "Task Name",
            'desc': "Description",
            'due_date': "2023-12-28",
            'tags': "a,b",
            'status': "WORKING"
        }
        response = self.client.patch('/taskapi/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.data['msg'], "Task Updated Partial")

    def test_task_update_partially_fail(self):
        Task.objects.create(title="Task Name", desc="Description", due_date="2023-12-28", tags="a,b", status="OPEN")

        data = {
            'title': "Task 2",
            'desc': "Description 2",
            'due_date': "2023-12-16",
            'tags': "a,b",
            'status': "WORKING"
        }
        response = self.client.patch('/taskapi/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_task_delete(self):
        Task.objects.create(title="Task Name", desc="Description", due_date="2023-12-28", tags="a,b", status="OPEN")
        response = self.client.delete('/taskapi/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['msg'], "Task Deleted")
