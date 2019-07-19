from django.db import models
from django.contrib import admin
from django.utils.timezone import datetime
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    manager     =   models.ForeignKey(User,on_delete=models.CASCADE,default=None,blank=True)
    name        =   models.CharField(max_length=50)
    email       =   models.EmailField(max_length=254)
    phone       =   models.IntegerField()
    info        =   models.CharField(max_length=150)
    gender      =   models.CharField(max_length=50,)
    image       =   models.ImageField(upload_to='img/',blank=True)
    # date_added  =   models.DateField(auto_now_add=True)
    date_added  =   models.DateTimeField(default=datetime.now)
    def __str__(self):
        return "Name: {} , Email {}".format(self.name,self.email)
    
    class Meta:
        ordering=['-id']
