from django.contrib import admin

# Register your models here.
from .models import Customer,Supplier,Carousel
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Carousel)