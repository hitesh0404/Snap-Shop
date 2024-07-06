from django.shortcuts import render,get_object_or_404
from .models import Cart,Customer,Product
from django.contrib.auth.models import User

# Create your views here.
def add_to_cart(request,id):
    user_id = User.objects.get(username=request.user)
    customer_object = Customer.objects.get(user_id=user_id.id)
    product_object = Product.objects.get(id=id)
    print(customer_object)
    item , create =Cart.objects.get_or_create(user=customer_object,product=product_object)
    if create:
        print('item created')
    else:
        item.quantity+=1
        item.save()
    cart = Cart.objects.filter(user=customer_object)
    context={
        'cart':cart
        }
    return render(request,'cart/cart.html',context)