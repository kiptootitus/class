from django.db import models
from django.contrib.auth.models import User 
# Create your models here.  
class Room(models.Model):   
    # host = models.CharField(max_length=50)  
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    #participants = models.ManyToManyField(User, related_name='participants')
    
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