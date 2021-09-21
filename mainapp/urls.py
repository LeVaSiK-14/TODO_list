from django.urls import path
from .views import TaskListView, TaskCreateView, TaskDetailGenericView, registration_view

app_name = 'mainapp'


urlpatterns = [
    path('task-list/', TaskListView.as_view(), name='task-list'),
    path('task-create/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:id>/', TaskDetailGenericView.as_view()),
    path('register/', registration_view, name='register')
]