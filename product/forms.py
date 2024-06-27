from .models import Product
from django.forms import ModelForm
from django import forms

class login(forms.Form):
    usename = forms.CharField(max_length=20)


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'