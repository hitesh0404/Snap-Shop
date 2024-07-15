from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth import get_user_model

def mail_send_new(request,products,user):

    subject ="List of new Products"
    to = user.email
    message = 'Hey this are the new products avaible now on our website'
    from_ = settings.EMAIL_HOST_USER
    src="https://buffer.com/cdn-cgi/image/w=1000,fit=contain,q=90,f=auto/library/content/images/size/w600/2023/10/free-images.jpg"
    context={'name':user.username,'src':src, 'products':products}
    html_data = render_to_string('account/message.html',context)
    send_mail(subject=subject,html_message=html_data,message=message,from_email=from_, recipient_list=[to,])

def mail_send(request):
    subject=request.POST.get('subject')
    to = request.POST.get('to')
    message = request.POST.get('message')
    from_ = settings.EMAIL_HOST_USER
    send_mail(subject=subject,message=message,from_email=from_, recipient_list=[to,])
    return HttpResponse("Done,<a href='/account/mail' > send more</a>")
    

from . forms import *
# def register_user(request):
#     context = {
#         'form':RegisterForm()
#     }
#     return render(request,'account/register_user.html',context)
from django.views import View

class Register(View):
    
    def get(self,request,user_type):
        if user_type not in ['supplier', 'customer']:
            return redirect('home')  # Redirect to a default page if user_type is invalid

        form_class = SupplierRegisterForm if user_type == 'supplier' else CustomerRegisterForm
        form_class
        context = {
                'user_form':RegisterForm(),
                'form':form_class(),
                'user_type':user_type
                       }
        return render(request,'account/register_user.html',context)
    
        
    def post(self,request,user_type):
        if user_type not in ['supplier', 'customer']:
            return redirect('home')  # Redirect to a default page if user_type is invalid
        user_form = RegisterForm(request.POST)
        form_class = SupplierRegisterForm if user_type == 'supplier' else CustomerRegisterForm
        form = form_class(request.POST)
        if form.is_valid() and user_form.is_valid():
            user = user_form.save()
            u = form.save(commit=False)
            u.user = get_object_or_404(User,pk=user.id)
            u.save()
        return redirect('home')
        
                # username=request.POST.get('username')
                # password = request.POST.get('password')
                # firstname = request.POST.get('first_name')
                # lastname = request.POST.get('last_name')
                # from django.contrib.auth.models import User
                # u = User.objects.create_user(username=username,password=password)
                # u.first_name = firstname
                # u.last_name = lastname
                # u.save()
               
       
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404

class Login(View):
    def get(self,request):
        return render(request,'account/login.html')
    def post(self,request,user_type):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        # user = User.objects.get(username=username) 
        # user =get_user_model().objects.get(username=username)
        user=User.objects.get(username=username) 
        user=1
        if user:
            # print(request.__dict__)
            u = authenticate(request,username=username,password=password)
            if u:
                login(request,u)
                if 'user_type' not in request.session:
                    request.session['user_type']=user_type
                messages.success(request,'welcome back to the Home page')
                return redirect('home')
            else:
                messages.error(request,'Wrong Username/Password')
             
                return render(request,'account/login.html')
        else:
            messages.error(request,'Wrong Username')
            return render(request,'account/login.html')

        return redirect('home')
        
            
def logout_user(request):
    logout(request)
    return  redirect('home')

def mail_send_new(request,products,user):
    pass