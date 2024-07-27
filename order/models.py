from django.db import models
from account.models import Address
from django.contrib.auth.models import User
# Create your models here.

class OrderStatus(models.Model):
    info = models.CharField(max_length=50)
    status = models.CharField(max_length=50, blank=False, null=False)
    
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    address = models.ForeignKey(Address,on_delete=models.DO_NOTHING)
    order_date = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.ForeignKey(OrderStatus,on_delete=models.DO_NOTHING)
    
    # payment_id = models.
    # order_status_id = models.
    # shipping_id = models.   
    def __str__(self):
        return (f'Customer: {self.user} and Order Value: {self.total} ')    

from product.models import Product
class Orderitem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    discount = models.ForeignKey(null=True,on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    refundable = models.BooleanField(default=True)

reason_choice=(
    ('1','Product Not Received'),
    ('2','Product Damaged'),
    ('3','Product Not as Described'),
    ('4','Other'),
)

class OrderRefund(models.Model):
    order_item = models.ForeignKey(Orderitem, on_delete=models.CASCADE)
    status       = models.CharField(max_length=50)
    reason       = models.IntegerField(max_length=1,choices=reason_choice)
    raised_date  = models.DateTimeField(auto_now_add=True)
    settled_date = models.DateTimeField()
    description  = models.TextField()