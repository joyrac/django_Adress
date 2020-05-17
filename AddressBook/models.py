from __future__ import unicode_literals  
from django.db import models  
# from django.db import models

# Create your models here.
# from django.db import models  
  
class Users(models.Model):  
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)
    DOB = models.DateField()
    mobile =  models.IntegerField(unique=True)
    email  = models.EmailField(max_length=50,unique=True)
    city = models.CharField(max_length=30)  
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)  
    pin = models.IntegerField()
    user_name = models.CharField(max_length=20,unique=True)  
    password = models.CharField(max_length=30)
    class Meta:  
        db_table = "Users"   
        
    