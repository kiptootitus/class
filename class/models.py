from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from django.urls import reverse
from django.db.models.deletion import CASCADE
# Create your models here.  


class Topic(models.Model):  
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
class Room(models.Model):   
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)   
    updated= models.DateTimeField(auto_now=True)    
    created= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name   

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    updated= models.DateTimeField(auto_now=True)    
    created= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body 