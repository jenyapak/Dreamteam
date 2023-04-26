from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet, TaskList, TaskDetail, UserCreate



router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserCreate.as_view(), name='user_create'),
    path('tasks/', TaskList.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
]
