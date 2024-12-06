from django.shortcuts import render
# views.py
from .models import Bruh

def homepage(request):
    data = Bruh.objects.all()  # Get all records from the Bruh model
    return render(request, 'homepage.html', {'data': data})

def products(request):
    return render(request, 'products.html')

def delivery(request):
    return render(request, 'delivery.html')

def mission_vision(request):
    return render(request, 'mission_vision.html')

def feedback(request):
    return render(request, 'feedback.html')

# Create your views here.
