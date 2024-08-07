from django.db import models
from django.contrib.auth.models import User
from order.models import Order
# Create your models here.
PAYMENT_STATUS_CHOICE = (
    ('pending','pending'),
    ('processing','processing'),
    ('completed','completed')
)
PAYMENT_METHOD_CHOICE = (
    ('RazorPay','RazorPay'),
    ('card','card'),
    ('COD','COD'),
    ('UPI','UPI'),
    ('net_banking','net_banking')
)
class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    payment_signature = models.CharField(max_length=64,default='')
    payment_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(decimal_places=2,max_digits=12)
    status = models.CharField(choices=PAYMENT_STATUS_CHOICE,max_length=20,default='pending')
    method = models.CharField(max_length=20,choices=PAYMENT_METHOD_CHOICE)
    order = models.ForeignKey(Order,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.user + ' paid ' + self.amount + ' on ' + self.last_update + ' and current status is ' + self.status
class Coupon(models.Model):
    code = models.CharField(max_length=30)
    details = models.CharField(max_length=100)
    discount_amount = models.PositiveIntegerField()
    validity_period = models.DateField()
    usage_limit = models.PositiveIntegerField()
    def __str__(self):
        return self.code
    
class CouponUsage(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    coupon = models.ForeignKey(Coupon,on_delete=models.CASCADE)
    used_date = models.DateTimeField(auto_now_add=True)  
    class Meta:
        unique_together = [['user','coupon']]
    
    def __str__(self):
        return self.user + ' used ' + self.coupon
