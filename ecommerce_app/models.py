from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=100)

class Products(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to='image/')
    brand=models.CharField(max_length=100)
    price=models.IntegerField()

class Customer(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)    
    phone_number=models.IntegerField(null=True)
    address=models.TextField(null=True)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Products,on_delete=models.CASCADE,null=True)
    
