from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import CustomerSupport

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email', 'password1','password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']

class CustomerSupportForm(ModelForm):
    class Meta:
        model = CustomerSupport
        fields = ['name','phone', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }

