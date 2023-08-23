from django.db import models

# Create your models here.  
class Room(models.Model):   
    host = models.CharField(max_length=50)  
    guest = models.CharField(max_length=50)
    name = models.CharField(max_length=50)