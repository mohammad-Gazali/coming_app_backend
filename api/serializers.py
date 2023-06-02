from rest_framework import serializers
from django.contrib.auth.models import User
from api import models



class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "is_superuser", "groups"]
        