from django.urls import path
from . import views

urlpatterns = [
    path('show_product/',views.showProduct,name= 'show-product'),
    path('add_product/',views.add_product,name='add-product'),
    path('product_details/<int:id>/',views.product_details,name='product-detail'),
    path('product_details/delete/<int:id>/',views.delete_product,name='delete-product'),
    path('product_details/update/<int:id>/',views.update_product,name='update-product'),

]