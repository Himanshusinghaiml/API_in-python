from django.shortcuts import render
from django.http import HttpResponse
from .models import logintable  # Assuming your model is named logintable

def home(request):
    if request.method == 'POST':  # Use 'POST' in uppercase
        username = request.POST.get('username')  # Use 'POST' in uppercase
        password = request.POST.get('password')
        contact = request.POST.get('contact')
        # Assuming your model is named logintable
        save_data = logintable(username=username, password=password, contact=contact)
        save_data.save()
        
        return HttpResponse("Data saved successfully")

    return render(request, "crud.html")
