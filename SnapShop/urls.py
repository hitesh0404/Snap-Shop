"""
URL configuration for SnapShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',TemplateView.as_view(template_name='index.html'),name='home'),
    path('',views.home,name='home'),

    path("about_us/", TemplateView.as_view(template_name="about.html"),name='about'),
    path('contact_us/',TemplateView.as_view(template_name='contact-us.html'),name ='contact'),
    path('home',views.home),
    path('product/',include('product.urls')),
    path('account/',include('account.urls')),
    path('cart/',include('cart.urls')),

]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, 
                        document_root=settings.MEDIA_ROOT)

