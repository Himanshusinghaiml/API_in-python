# serializers.py
from rest_framework import serializers
from .models import logintable
from .models import student

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = logintable
        fields = ['username', 'password', 'contact']
        
class studentdata(serializers.ModelSerializer):
    class Meta:
        model=student
        fields = '__all__' 
        
