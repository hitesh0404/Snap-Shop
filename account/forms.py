from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *

class RegisterForm(ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password']
    field_order =  ['first_name','last_name','username','email','password']
    
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["password"].widget.attrs.update({
            
    #         "type": "password"
    #     })

class CustomerRegisterForm(ModelForm):

    class Meta:
        model=Customer
        exclude = ['user']

class SupplierRegisterForm(ModelForm):

    class Meta:
        model=Supplier
        exclude = ['user']