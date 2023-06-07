from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUp(UserCreationForm):
    class meta:
        model=User
        fields=['Username','email','password1','password2']

class loginForm(forms.Form):
    email=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


