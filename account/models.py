from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Customer(models.Model):
    user  = models.OneToOneField(to=User,on_delete=models.CASCADE)