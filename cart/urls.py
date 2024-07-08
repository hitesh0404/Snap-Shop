from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<int:id>',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.cart,name='cart')
]
