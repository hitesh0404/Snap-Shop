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
    def get(self,request,user_type):
        if user_type not in ['supplier', 'customer']:
            messages.error(request,'Not a valid User Type')
            return redirect('login' 'login')  # Redirect to a default page if user_type is invalid
        return render(request,'account/login.html', {'user_type':user_type})
    def post(self,request,user_type):
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username,password)
        # user = User.objects.get(username=username) 
        # user =get_user_model().objects.get(username=username)
        user=User.objects.get(username=username) 
        # user=1
        if user:
            # print(request.__dict__)
            u = authenticate(request,username=username,password=password)
            if u and 'user_type' not in request.session:
                if user_type == 'customer':
                    if hasattr(u,'customer'):
                        request.session['user_type']='customer'
                        request.session['user_email']= user.email
                        cust_obj = Customer.objects.get(user=user.id)
                        request.session['contact']= cust_obj.phone_number
                elif user_type=='supplier':
                    if hasattr(u,'supplier'):
                        request.session['user_type']='supplier'
                        request.session['user_email']= user.email
                        supp_obj = Supplier.objects.get(user=user.id)
                        request.session['contact']= supp_obj.phone_number
                login(request,u)
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


def choice_for_user(request,request_for):
    context={
        'request_for':request_for
    }
    return render(request,'account/choice.html',context)
import random
def reset_password(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        user  = get_object_or_404(User,username = username)
        if user:
            request.session['email']= user.email
            request.session['username']= user.username
            request.session['reset_password_attemp_count']=3
            print(request.session)
            return render(request,'account/take_email.html')
    if request.method =='POST':
        email = request.POST.get('email')
        print(email)
        if email == request.session.get('email'):
            otp = random.randint(1000,9999)
            print(otp)
            request.session['otp']=otp
            return render(request,'account/verify_otp.html')
    return  redirect('home')

def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        print(otp)
        if request.session.get('reset_password_attemp_count')>0:
            request.session['reset_password_attemp_count']==request.session.get('reset_password_attemp_count')-1
            if int(otp) == request.session.get('otp'):

                return render(request,'account/change_password.html')
            else:
                return render(request,'account/verify_otp.html')
        else:
            return redirect('home')
    return redirect('home')
    
            
def change_password(request):
    if request.method == 'POST':
        password = request.POST.get('new_password')
        print(password)
        username = request.session.get('username')
        user  = get_object_or_404(User,username = username)
        user.set_password(password)
        user.save()
        return  redirect('home')
        