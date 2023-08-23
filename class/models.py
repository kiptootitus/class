from django.db import models

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