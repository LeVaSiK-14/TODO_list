from django.shortcuts import render
from .models import Task
from .serializers import UserSerializer, TaskSerializers, TaskCreateSerializers, UserRegSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers, status, views, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

User = get_user_model()

class TaskListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializers

class TaskDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    lookup_field = 'id'


@api_view(["POST", ])
def registration_view(request):

    if request.method == "POST":
        serializer = UserRegSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully registered a new user.'
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)