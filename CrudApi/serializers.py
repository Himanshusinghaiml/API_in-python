# serializers.py
from rest_framework import serializers
from .models import logintable

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = logintable
        fields = ['username', 'password', 'contact']
