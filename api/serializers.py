from dataclasses import field
from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  
    

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')

    def create(self, validated_data):                                   #override function to create user and encrypt password 
        user = User.objects.create_user(**validated_data)
        return user                                                     

