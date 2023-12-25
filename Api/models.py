# from datetime import date
from django.db import models
from django.forms import ValidationError

Task_Status = ["OPEN", "WORKING", "DONE", "OVERDUE"]
Task_Status_Sorted = sorted([(item, item) for item in Task_Status])


class Task(models.Model):
    title = models.CharField(max_length=100, blank=True)
    desc = models.TextField(blank=True)
    time_stamp = models.DateField(auto_now_add=True, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=100, default="OPEN", choices=Task_Status_Sorted, blank=True)

    # function to split tags
    def tag_list(self):
        taglist = self.tags.split(',')
        return taglist

    # logic for due_date
    def clean(self):
        super().clean()

        if self.due_date < self.time_stamp:
            raise ValidationError("Due date must be greater than current date")
