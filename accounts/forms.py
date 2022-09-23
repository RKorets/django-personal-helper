from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm


from captcha.fields import CaptchaField


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='')

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2', 'captcha'
        ]


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UpdateUserForm(forms.Form):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))


class PasswordProfileForm(forms.Form):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class PasswordProfileFormBasic(PasswordChangeForm):

    old_password = forms.CharField(label='Old password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        fields = [
            'old_password', 'new_password1', 'new_password2'
        ]
