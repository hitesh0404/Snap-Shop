from django.shortcuts import render,get_object_or_404,redirect
from .models import Cart,Customer,Product
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from payment.models import Payment
from order.models import Order,Orderitem
import uuid
import razorpay



def get_objects(request,slug):
    user_obj = User.objects.get(username=request.user)
    cust_obj = Customer.objects.get(user=user_obj.id)
    prod_obj = Product.objects.get(slug=slug)
    return cust_obj,prod_obj


@login_required
def update_quantity(cust_obj,product_id,quantity):
    item = Cart.objects.get(user=cust_obj,product=product_id)
    item.quantity=int(quantity)
    item.save()
    return None





@login_required
def add_to_cart(request,slug):
    cust_obj,prod_obj = get_objects(request,slug)
    item , create =Cart.objects.get_or_create(user=cust_obj,product=prod_obj)
    if create:
        print('item created')
    else:
        item.quantity+=1
        item.save()
    return cart(request,cust_obj)

@login_required
def update_cart(request,id):
    customer_object= Customer.objects.get(user_id=request.user.id)
    for product_id,quantity in request.GET.items():
        update_quantity(customer_object,product_id,quantity)
    cart = Cart.objects.filter(user=customer_object)
    context={
        'cart':cart
        }
    return render(request,'cart/cart.html',context)

@login_required
def cart(request,customer_object='default'):   
    if customer_object =='default':
        customer_object= Customer.objects.get(user_id=request.user.id)
    cart = Cart.objects.filter(user=customer_object)
    context={
        'cart':cart
        }
    return render(request,'cart/cart.html',context)

@login_required
def increase_quantity(request,id,amount=1):
    cust_obj,prod_obj = get_objects(request,id)
    item = Cart.objects.get(user=cust_obj,product=prod_obj)
    item.quantity+=amount
    item.save()
    return cart(request,cust_obj)
    

@login_required
def remove_product_from_cart(request,id):
    cust_obj,prod_obj = get_objects(request,id)
    item = Cart.objects.get(user=cust_obj,product=prod_obj)
    item.delete()
    return cart(request,cust_obj)
    

@login_required
def decrease_quantity(request,id,amount=1):
    cust_obj,prod_obj = get_objects(request,id)
    item = Cart.objects.get(user=cust_obj,product=prod_obj)
    if item.quantity>amount:
        item.quantity-=amount
        item.save()
    else:
        item.delete()
    return cart(request,cust_obj)

@login_required
def clear_cart(request):
    cust_obj = Customer.objects.select_related('user').get(user=request.user.id)
    Cart.objects.filter(user=cust_obj).delete()
    return render(request,'cart/cart.html')
@login_required
def checkout(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            od_id=uuid.uuid4().hex
            order_obj = form.save(commit=False)
            order_obj.uuid = str(od_id)   
            order_obj.save()
            user_obj = User.objects.get(username=request.user)
            cust_obj = Customer.objects.get(user=user_obj.id)
            cart_obj = Cart.objects.filter(user = cust_obj )
            total=0
            for item in cart_obj:
                price= Product.objects.get(id = item.product.id).price
                total = total + (item.quantity * price)
                order_item_obj = Orderitem(order=order_obj,product=item.product,quantity = item.quantity,price  =price)
                order_item_obj.save()
            # cart_obj.delete()
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

            order_obj.total = int(total*100)

            data = { "amount": (int(total*100)), "currency": "INR", "receipt": order_obj.uuid }
            payment = client.order.create(data=data)
            order_obj.payment_id = payment.get('id')       
            print('here',payment.get('id'),'here')     
            order_obj.save()
            print(payment,order_obj,order_item_obj)
            context = {
                'order':order_obj,
                'total':total,
                'payment':payment   
            }
            order_obj.__dict__
            return render(request,'cart/payment.html',context)
    else:
        form = OrderForm()
        return render(request,'cart/checkout.html',{'form':form})

@csrf_exempt
@login_required
def success(request):
    if request.method == "POST":
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        params_dict = {
            'razorpay_order_id': request.POST.get('razorpay_order_id'),
            'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
            'razorpay_signature': request.POST.get('razorpay_signature')
        }

        try:
            client.utility.verify_payment_signature(params_dict)
            user_obj = User.objects.get(username=request.user)
            order_id = params_dict['razorpay_order_id']
            print(order_id)
            order = Order.objects.get(payment_id=order_id)
            amount = order.total
            payment_method = 'RazorPay'
            Payment.objects.create(
                user=user_obj,
                payment_signature=params_dict['razorpay_signature'],
                amount=amount / 100,  
                status='completed',
                method=payment_method,
                order=order
            )

            cust_obj = Customer.objects.get(user=user_obj.id)
            cart_obj = Cart.objects.filter(user=cust_obj)
            cart_obj.delete()

            
            return render(request, 'cart/success.html')
        
        except razorpay.errors.SignatureVerificationError:
            return HttpResponseBadRequest("Signature verification failed")
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    return HttpResponseBadRequest("Invalid request")


















# def success(request):
#     import razorpay
#     client = razorpay.Client(auth=("YOUR_ID", "YOUR_SECRET"))

#     client.utility.verify_payment_signature({
#    'razorpay_order_id': razorpay_order_id,
#    'razorpay_payment_id': razorpay_payment_id,
#    'razorpay_signature': razorpay_signature
#    })
#     user_obj = User.objects.get(username=request.user)
#     cust_obj = Customer.objects.get(user=user_obj.id)
#     cart_obj = Cart.objects.filter(user = cust_obj )
#     cart_obj.delete()
#     return render(request,'cart/success.html')
