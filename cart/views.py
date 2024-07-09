from django.shortcuts import render,get_object_or_404,redirect
from .models import Cart,Customer,Product
from django.contrib.auth.models import User



def get_objects(request,id):
    user_obj = User.objects.get(username=request.user)
    cust_obj = Customer.objects.get(user=user_obj.id)
    prod_obj = Product.objects.get(id=id)
    return cust_obj,prod_obj



# Create your views here.
def add_to_cart(request,id):
    cust_obj,prod_obj = get_objects(request,id)

    item , create =Cart.objects.get_or_create(user=cust_obj,product=prod_obj)
    if create:
        print('item created')
    else:
        item.quantity+=1
        item.save()
    return cart(request,cust_obj)
    


def cart(request,customer_object='default'):
    
    if customer_object =='default':
        customer_object= Customer.objects.get(user_id=request.user.id)
    cart = Cart.objects.filter(user=customer_object)
    context={
        'cart':cart
        }
    return render(request,'cart/cart.html',context)


def increase_quantity(request,id):
    cust_obj,prod_obj = get_objects(request,id)
    item = Cart.objects.get(user=cust_obj,product=prod_obj)
    item.quantity+=1
    item.save()
    return cart(request,cust_obj)
    


def remove_product_from_cart(request,id):
    cust_obj,prod_obj = get_objects(request,id)
    item = Cart.objects.get(user=cust_obj,product=prod_obj)
    item.delete()
    return cart(request,cust_obj)
    


def decrease_quantity(request,id):
    cust_obj,prod_obj = get_objects(request,id)
    item = Cart.objects.get(user=cust_obj,product=prod_obj)
    if item.quantity>1:
        item.quantity-=1
        item.save()
    else:
        item.delete()
    return cart(request,cust_obj)


def clear_cart(request):
    cust_obj = Customer.objects.select_related('user').get(user=request.user.id)
    Cart.objects.filter(user=cust_obj).delete()
    return render(request,'cart/cart.html')