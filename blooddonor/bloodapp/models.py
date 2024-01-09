from django.db import models

class UserProfile(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    blood=models.CharField(max_length=10)
    address=models.CharField(max_length=50)
    willing_to_donate=models.CharField(max_length=5)
       
class GetDonor(models.Model):
    blood=models.CharField(max_length=10)
    address=models.CharField(max_length=50)
    
    
    


# Create your models here.
