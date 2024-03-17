from django.db import models

class Users(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    username= models.CharField(max_length=30, unique=True,primary_key=True)
    email= models.EmailField(unique=True)
    phone= models.CharField(max_length=10)
    address= models.TextField()
    password= models.CharField(max_length=128)