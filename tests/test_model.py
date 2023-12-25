from django.test import TestCase
from Api.models import *
from django.core.exceptions import ValidationError

class TaskModelTest(TestCase):
    def test_create_task(self):
        title = "Task Name"
        desc = "Description"
        due_date = "2023-12-28"
        tags = "a,b"
        status = "OPEN"

        task = Task.objects.create(title=title, desc=desc, due_date=due_date, tags=tags, status=status)
        self.assertEqual(task.title, title)
        self.assertEqual(task.desc, desc)
        self.assertEqual(task.due_date, due_date)
        self.assertEqual(task.tags, tags)
        self.assertEqual(task.status, status)

    def test_due_date_validation(self):
        title = "Task Name"
        desc = "Description"
        due_date = "2023-12-16"
        tags = "a,b"
        status = "OPEN"

        task = Task.objects.create(title=title, desc=desc, due_date=due_date, tags=tags, status=status)
        self.assertRaises(ValidationError, task.full_clean)

    def test_tags_list(self):
        title = "Task Name"
        desc = "Description"
        due_date = "2023-12-28"
        tags = "a,b"
        status = "OPEN"

        task = Task.objects.create(title=title, desc=desc, due_date=due_date, tags=tags, status=status)
        self.assertEqual(task.tag_list(), ['a', 'b'])
