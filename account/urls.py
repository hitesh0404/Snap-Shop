from django.urls import path

from django.views.generic import TemplateView
from . import views
urlpatterns = [
path('mail/',TemplateView.as_view(template_name='account/email_form.html'),name='get_email_form'),
path('send_mail/',views.mail_send,name='mail_send'),
path('register_customer/<str:user_type>/',views.Register.as_view(),name='register-customer'),
path('register_supplier/<str:user_type>/',views.Register.as_view(),name='register-supplier'),
path('choice/',TemplateView.as_view(template_name='account/choice.html'),name='choice'),
path('login_user/',views.Login.as_view(),name='login-user'),
path('logout_user/',views.logout_user,name='logout-user'),

]