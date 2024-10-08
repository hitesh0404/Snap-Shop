from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views
urlpatterns = [
path('mail/',TemplateView.as_view(template_name='account/email_form.html'),name='get_email_form'),
path('send_mail/',views.mail_send,name='mail_send'),
path('register_customer/<str:user_type>/',views.Register.as_view(),name='register_user'),
path('choice/<str:request_for>',views.choice_for_user,name='login'),
path('choice/<str:request_for>',views.choice_for_user,name='register'),
path('login_user/<str:user_type>',views.Login.as_view(),name='login_user'),
path('logout_user/',views.logout_user,name='logout-user'),
path('reset_password/',views.reset_password,name='reset-password'),
path('verify_otp/',views.verify_otp,name='verify_otp'),
path('change_password/',views.change_password,name='change_password'),
]