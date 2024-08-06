from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<int:id>',views.add_to_cart,name='add_to_cart'),
    path('increase_quantity/<int:id>/',views.increase_quantity,name='increase-quantity'),
    path('decrease_quantity/<int:id>/',views.decrease_quantity,name='decrease-quantity'),
    path('remove_product_from_cart/<int:id>/',views.remove_product_from_cart,name='remove-product-from-cart'),
    path('clear_cart/',views.clear_cart,name='clear-cart'),
    path('cart/',views.cart,name='cart'),
  path('checkout',views.checkout,name='checkout'),
]
