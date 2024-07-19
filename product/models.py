from django.db import models

# Create your models here.

  
class Brand(models.Model):
    pass
class Category(models.Model):
    pass

class Product(models.Model):#product_product
    name = models.CharField(max_length=25)
    price  = models.DecimalField(decimal_places=2,max_digits=10)
    desc = models.TextField()
    image = models.ImageField(upload_to='product/',default="product/online-shopping-background-website-mobile-app_269039-166.jpg")
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    class Meta:
        db_table = 'Product'
        ordering = ['name']
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    pass
class Category(models.Model):
    pass