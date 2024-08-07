from django.db import models
from account.models import Address
from django.contrib.auth.models import User
from product.models import Product
# Create your models here.

class OrderStatus(models.Model):
    info = models.CharField(max_length=50)
    status = models.CharField(max_length=50, blank=False, null=False)
SHIPPING_METHOD_CHOICES = (
    ('standard', 'Standard Shipping'),
    ('express', 'Express Shipping'),
    ('overnight', 'Overnight Shipping'),
    ('pickup', 'In-Store Pickup'),
    ('courier', 'Courier Service'),
    ('international', 'International Shipping'),
) 
SHIPPING_CHARGES_CHOICES = {
    'standard':100,
    'express':200,
    'overnight':500,
    'pickup':0,
    'courier':700,
    'international':10000,
}
class Shipping(models.Model):
    method = models.CharField(choices=SHIPPING_METHOD_CHOICES,max_length=20)
    charges = models.IntegerField(default=0)
    def save(self,*args,**kwargs):
        self.charges = SHIPPING_CHARGES_CHOICES.get(self.method)
        super(Shipping,self).save(*args,**kwargs)
    def __str__(self) -> str:
        return self.method +' ' + str(self.charges)
class Order(models.Model):
    uuid = models.CharField(max_length=128,default='0',)
    payment_id = models.CharField(max_length=100,default=0)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    address = models.ForeignKey(Address,on_delete=models.DO_NOTHING)
    order_date = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.ForeignKey(OrderStatus,on_delete=models.DO_NOTHING)
    shipping_id = models.ForeignKey(Shipping,on_delete=models.DO_NOTHING)
    class Meta:
        indexes = [
            models.Index(fields=['uuid'])
        ]
    def __str__(self):
        return (f'Customer: {self.user} and Order Value: {self.total} ')    

class Discount(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    code = models.CharField(max_length=10, unique=True)
    discount_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.code
    



from product.models import Product

class Orderitem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    discount = models.ForeignKey(Discount,null=True,on_delete=models.DO_NOTHING)
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