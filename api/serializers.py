from rest_framework import serializers
from .models import Task
from .models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "user", "task", "completed"]


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password")

    def create(
        self, validated_data
    ):  # override function to create user and encrypt password
        user = User.objects.create_user(**validated_data)
        return user
