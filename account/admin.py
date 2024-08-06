from django.contrib import admin

# Register your models here.
from .models import Customer,Supplier,Carousel,Address
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Address)
admin.site.register(Carousel)