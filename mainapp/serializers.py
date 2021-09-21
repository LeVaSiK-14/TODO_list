from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Task



User = get_user_model()

class TaskCreateSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ['user', 'title', 'description', 'dead_line', 'status', 'start_date']


class TaskSerializers(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'dead_line', 'status', 'start_date']


class UserSerializer(serializers.ModelSerializer):
    tasks = TaskSerializers(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'tasks']

class UserRegSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'password2']
        extra_kwargs = {
            'password' :{"write_only": True}
        }
    def save(self):
        user = User(
            username=self.validated_data['username'],
            
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user
