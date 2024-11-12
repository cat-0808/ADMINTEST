from django.db import models
# models.py
from django.db import models

class Bruh(models.Model):
    name = models.CharField(max_length=100)  # Product name  # Product description
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    description = models.TextField() # Product price
    stock = models.IntegerField()


    def __str__(self):
        return self.name

# Create your models here.
