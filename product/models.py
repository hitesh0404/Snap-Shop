from django.db import models
from autoslug import AutoSlugField

# Create your models here.

    
class Brand(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo')
    def __str__(self) -> str:
        return self.name

# CATEGORY_CHOICES = [
#         ('ELECTRONICS', 'Electronics'),
#         ('CLOTHING', 'Clothing'),
#         ('BOOKS', 'Books'),]
class Category(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    description = models.TextField()
    def __str__(self) -> str:
        return self.name

class Product(models.Model):#product_product
    name = models.CharField(max_length=25)
    slug = AutoSlugField(populate_from = 'name',blank=True,null=True,unique=True)
    price  = models.DecimalField(decimal_places=2,max_digits=10)
    desc = models.TextField()
    image = models.ImageField(upload_to='product/',default="product/online-shopping-background-website-mobile-app_269039-166.jpg")
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category,db_table='Product_Category_New')
    quantity = models.IntegerField(default=1)
    class Meta:
        db_table = 'Products'
        ordering = ['name']
    def __str__(self):
        return self.name
  
from django.contrib.auth.models import User


class Reviews(models.Model):
    title = models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    rating = models.IntegerField()
    review = models.TextField()
    def __str__(self):
        return self.title
    class Meta:
        unique_together=(('user','product'))