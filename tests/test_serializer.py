from Api.serializers import TaskSerializer
from rest_framework.test import APITestCase


class TaskSerializerTest(APITestCase):
    def test_task_serializer_valid_data(self):
        data = {
            'title': "Task Name",
            'desc': "Description",
            'due_date': "2024-06-28",
            'tags': "a,b",
            'status': "OPEN"
        }
        serializer = TaskSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors, {})

    def test_task_serializer_due_date_validation(self):
        data = {
            'title': "Task Name",
            'desc': "Description",
            'due_date': "2023-12-16",
            'tags': "a,b",
            'status': "OPEN"
        }
        serializer = TaskSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors['non_field_errors'][0], "Due date should be greater than timestamp")
