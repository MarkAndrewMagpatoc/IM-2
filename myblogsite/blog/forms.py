from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

# Signup form
class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

# Signin form (using Django's built-in form)
class SigninForm(AuthenticationForm):
    pass