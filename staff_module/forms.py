from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Firstname', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your fristname'}))
    last_name = forms.CharField(label='Lastname', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your lastname'}))
    username = forms.CharField(label='Username', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
    phonenumber = forms.CharField(label='Mobile', min_length=10, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter a valid number'}))
    password1 = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password must be strong'}))
    email = forms.EmailField(label='Email', max_length=200, required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter a valid email-id'}))
    password2 = forms.CharField(label='Confirm password', required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the same password as above'}))
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phonenumber',
                  'username', 'email', 'password1', 'password2']





class LoginForm(forms.Form):
    email = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control mt-2 mb-2', 'placeholder': 'Enter Email'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control mt-2 mb-2', 'placeholder': 'Enter password'}))

class AddStaff(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phonenumber',
                  'email', 'password']

class EditStaff(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phonenumber',
                  'email']
