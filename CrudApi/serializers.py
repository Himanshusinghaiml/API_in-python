# serializers.py
from rest_framework import serializers
from .models import logintable
from .models import student,himanshu

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = logintable
        fields = ['username', 'password', 'contact']
        
class studentdata(serializers.ModelSerializer):
    class Meta:
        model=student
        fields = '__all__' 
        
class himanshuserializer(serializers.ModelSerializer):
    class Meta:
        model=himanshu
        fields='__all__'
        
 
    def validate_name(self, value):
        # Example: Ensure that the name is not empty
        if not value:
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_branch(self, value):
        #  Ensure that the branch is a valid choice
        valid_branches = ["CSE-IT", "CSE", "AIML"]   
        if value not in valid_branches:
            raise serializers.ValidationError(f"Invalid branch. Choose from {', '.join(valid_branches)}.")
        return value
 

    def validate(self, data):
        if len(data['address']) < 5:
            raise serializers.ValidationError("Address must be at least 5 characters long.")
        return data
