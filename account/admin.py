from django.contrib import admin

# Register your models here.
from .models import Customer,Supplier

admin.site.register(Customer)
admin.site.register(Supplier)