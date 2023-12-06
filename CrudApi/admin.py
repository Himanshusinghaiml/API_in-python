from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import logintable  # Import your model

# Register your model with the admin site
@admin.register(logintable)
class logintableAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'contact')  # Define fields to display in the admin list view
