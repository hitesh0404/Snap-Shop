from django.shortcuts import render,redirect,get_object_or_404
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product
from account.views import mail_send_new

# @login_required
def showProduct(request):
    products = Product.objects.all()
    context={
        'products': products
    }
    u=get_object_or_404(User,pk=10)
    mail_send_new(request,products,u)
    return render(request,'product/show_product.html',context)


def add_product(request):
    print(request.POST,request.GET)
    if request.method =="POST":
        form =  ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {
                'form': form
            }
            
            return render(request,'product/add_product.html',context)
    elif request.method=="GET":
        context = {
            'form': ProductForm()
        }
        print('get view')
        return render(request,'product/add_product.html',context)


def product_details(request,id):
    context = {
        'p':get_object_or_404(Product,pk=id)
    }
    return render(request,'product/product_details.html',context)


def delete_product(request,id):
    p = get_object_or_404(Product,pk=id)
    if p:
        if request.method=="GET":
            return render(request,'confirm_delete.html',{'object':p})
        elif request.method == "POST":
            p.delete()
            return redirect('show-product')
    
    
def update_product(request,id):
    p = get_object_or_404(Product,pk=id)
    if request.method =='GET':
        form = ProductForm(instance=p)
        return render(request,'product/update_product.html',{'form':form})
    elif request.method=='POST':
        form = ProductForm(request.POST,instance=p)
        if form.is_valid():
            form.save()
            return product_details(request,id)
        else:
            return render(request,'product/update_product.html',{'form':form})


def add_to_cart(request,id):
    return redirect('home')
