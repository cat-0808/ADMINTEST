from django.shortcuts import render
# views.py
from .models import Bruh

def homepage(request):
    data = Bruh.objects.all()  # Get all records from the Bruh model
    return render(request, 'homepage.html', {'data': data})

# Create your views here.
