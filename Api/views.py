from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework import viewsets


class TaskViewSet(viewsets.ViewSet):
    # function to show/list/respond all tasks or data
    def list(self, request):
        tasks = Task.objects.all()
        serialized = TaskSerializer(tasks, many=True)
        return Response(serialized.data)

    # function to show/respond single data with id
    def get(self, request, pk=None):
        id = pk
        if id is not None:
            task = Task.objects.get(pk=id)
            serialized = TaskSerializer(task)
            return Response(serialized.data)

    # function to create/post new task/data
    def create(self, request):
        serialized = TaskSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response({'msg': 'Task Created'}, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    # function to perform complete update
    def update(self, request, pk):
        id = pk
        task = Task.objects.get(pk=id)
        serialized = TaskSerializer(task, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response({'msg': 'Task Updated'}, status=status.HTTP_202_ACCEPTED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    # function to perform partial update
    def partial_update(self, request, pk):
        id = pk
        task = Task.objects.get(pk=id)
        serialized = TaskSerializer(task, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response({'msg': 'Task Updated Partial'}, status=status.HTTP_202_ACCEPTED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    # function to delete data/task
    def delete(self, request, pk):
        id = pk
        task = Task.objects.get(pk=id)
        task.delete()
        return Response({'msg': 'Task Deleted'}, status=status.HTTP_200_OK)
