from django.db import models

# Create your models here.
class logintable(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    contact=models.CharField(max_length=100)
#to create and store new data in student table 
 
class student(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.IntegerField()
    branch=models.CharField(max_length=60)