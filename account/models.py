from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone
choice=(('M','Male'),('F','Female'),("O",'Other'))



class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    

class Customer(models.Model):
    user  = models.OneToOneField(to=User,on_delete=models.CASCADE)
    phone_number = models.BigIntegerField()
    profile_image = models.ImageField(upload_to='user_profile_pic/',default=r'C:\Users\admin\Django Project\Main Project Folder\media\images\product_image\random_cat.jpg')
    DOB = models.DateTimeField(default=timezone.now)
    user_create_date = models.DateTimeField(auto_now_add=True)
    profile_update_date= models.DateTimeField(auto_now=True,)
    gender = models.CharField(choices=choice,max_length=1)


class Supplier(models.Model):
    user  = models.OneToOneField(to=User,on_delete=models.CASCADE)
    phone_number = models.BigIntegerField()
    supplier_logo = models.ImageField(upload_to='supplier/logo/',default=r'C:\Users\admin\Django Project\Main Project Folder\media\images\product_image\random_cat.jpg')
    user_create_date = models.DateTimeField(auto_now_add=True)
    profile_update_date= models.DateTimeField(auto_now=True,)
    document_photo =models.ImageField(upload_to='supplier/document/',default=r'C:\Users\admin\Django Project\Main Project Folder\media\images\product_image\random_cat.jpg')
    company_name = models.CharField(max_length=30)

