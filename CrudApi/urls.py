from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Api.views import TaskViewSet

# Creating Router Object
router = DefaultRouter()

# Register TaskViewSet with Router
router.register('taskapi', TaskViewSet, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(router.urls)),
]
