from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField
# Create your models here.

class UserProfile(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    EmailField =models.CharField(max_length = 255, null=True, blank= True)
    
    
    def __str__(self):
        return str(self.user)
 