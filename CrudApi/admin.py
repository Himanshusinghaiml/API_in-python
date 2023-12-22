from django.contrib import admin
from .models import logintable, student,himanshu

@admin.register(logintable)
class logintableAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'contact')  # Define fields to display in the admin list view

@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'rollno', 'branch')  # Corrected the attribute name to list_display
    
admin.site.register(himanshu)
