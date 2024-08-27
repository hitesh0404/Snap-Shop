from django.shortcuts import render,redirect,get_object_or_404
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product,Category
from account.views import mail_send_new
from django.contrib import messages
from django.core.paginator import Paginator
# @login_required
def showProduct(request):
    products = Product.objects.all()
    paginate_obj = Paginator(products,8)
    page_number = request.GET.get('page')
    if not page_number :
        page_number =1
    paginate = paginate_obj.page(page_number)
    categories = Category.objects.all()
    
    context={
        'products': paginate.object_list,
        'categories':categories,
        'paginate':paginate,
        'range': range(2,paginate.paginator.num_pages)
    }
    u=get_object_or_404(User,pk=1)
    mail_send_new(request,products,u)
    print('mail')
    return render(request,'product/show_product.html',context)

@login_required
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


def product_details(request,slug):
    context = {
        'p':get_object_or_404(Product,slug=slug)
    }
    return render(request,'product/product_details.html',context)

@login_required
def delete_product(request,slug):
    p = get_object_or_404(Product,slug=slug)
    if p:
        if request.method=="GET":
            return render(request,'confirm_delete.html',{'object':p})
        elif request.method == "POST":
            p.delete()
            return redirect('show-product')
    
@login_required 
def update_product(request,slug):
    p = get_object_or_404(Product,slug=slug)
    if request.method =='GET':
        form = ProductForm(instance=p)
        return render(request,'product/update_product.html',{'form':form})
    elif request.method=='POST':
        form = ProductForm(request.POST,instance=p)
        if form.is_valid():
            form.save()
            return product_details(request,slug)
        else:
            return render(request,'product/update_product.html',{'form':form})

# @login_required
# def add_to_cart(request,slug):
#     return redirect('home')


def filter_by_category(request,name):
    # products = Product.objects.filter(category=name)
    c= get_object_or_404(Category,name=name)
    products = c.product_set.all()
    categories = Category.objects.all()

    context = {
        'products':products,
        'categories':categories
        }
    return render(request,'product/show_product.html',context)


def search_product(request):
    name = request.GET.get('search')
    products = Product.objects.filter(name__icontains=name)
    if not products.exists():
        messages.error(request,'No product found')
        products =Product.objects.filter(desc__icontains=name)
    categories = Category.objects.all()
    context = {
        'products':products,
        'categories':categories
        }
    
    return render(request,'product/show_product.html',context)