from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField
# Create your models here.

class UserProfile(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length = 255, null=True, blank= True)
    EmailField =models.CharField(max_length = 255, null=True, blank= True)
    avatar = models.ImageField(default= 'img.jpeg', blank= True,  null = True, upload_to= "images/profile")

    
    def __str__(self):
        return str(self.user)
 