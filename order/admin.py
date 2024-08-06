from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(OrderStatus)
admin.site.register(OrderRefund)
admin.site.register(Shipping)


