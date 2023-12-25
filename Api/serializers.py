from rest_framework import serializers
from .models import *
from datetime import date


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'desc', 'time_stamp', 'due_date', 'status', 'tags', 'tag_list']

    def validate(self, data):
        if data['due_date'] < date.today():
            raise serializers.ValidationError('Due date should be greater than timestamp')
        return data
