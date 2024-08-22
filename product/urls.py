from django.urls import path
from . import views

urlpatterns = [
    path('show_product/',views.showProduct,name= 'show-product'),
    path('add_product/',views.add_product,name='add-product'),
    path('product_details/<slug>/',views.product_details,name='product-detail'),
    path('product_details/delete/<slug>/',views.delete_product,name='delete-product'),
    path('product_details/update/<slug>/',views.update_product,name='update-product'),
    path('category/<str:name>/',views.filter_by_category,name='category'),
    path('search_product/',views.search_product,name='search_product'),
    # path('product_details/add_to_cart/<int:id>/',views.add_to_cart,name='add-to-cart'),
]