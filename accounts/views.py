# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
# from django.urls import reverse_lazy
# from django.views import generic
from .forms import RegisterUserForm, LoginUserForm, UpdateUserForm, PasswordProfileFormBasic
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
import os


# from django.core.mail import send_mail


def home(request):
    if request.user.is_authenticated:
        return redirect('news')
    return render(request, 'registration/home.html')


def user_logout(request):
    logout(request)
    return redirect('home')


def user_login(request):
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginUserForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'No valid input!')
    else:
        form = RegisterUserForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required(login_url='home')
def user_profile(request, pk):
    user = request.user.id
    pasw = PasswordProfileFormBasic(user=request.user)
    if user == pk:
        instance = User.objects.filter(pk=pk).first()
        form = UpdateUserForm(initial={'email': instance.email, 'username': instance.username})
        if request.method == 'GET':
            return render(request, "registration/profile.html", {'form': form, 'password_from': pasw})
        if request.method == 'POST':
            name = request.POST.get("username", None)
            if name is None:
                password_form = PasswordChangeForm(data=request.POST, user=request.user)
                if password_form.is_valid():
                    password_form.save()
                    update_session_auth_hash(request, request.user)
                    messages.success(request, 'Success update')
                    return render(request, "registration/profile.html", {'form': form, 'password_from': pasw})
                else:
                    messages.error(request, 'Password not valid')
                    return render(request, "registration/profile.html", {'form': form, 'password_from': pasw})
            else:
                form = UpdateUserForm(request.POST or None,
                                      initial={'email': instance.email, 'username': instance.username})
                if form.is_valid():
                    user_card = User.objects.filter(username=request.POST['username']).first()
                    if user_card is None or user_card.pk == request.user.id:
                        if user_card is not None and user_card.username == request.POST['username']:
                            e = User.objects.get(pk=request.user.id)
                            e.email = request.POST['email']
                            e.save()
                            messages.success(request, 'Success update')
                        else:
                            u = User.objects.get(pk=request.user.id)
                            u.username = request.POST['username']
                            u.email = request.POST['email']
                            u.save()

                            messages.success(request, 'Success update')
                    else:
                        messages.error(request, 'Profile name already exist')
                return render(request, "registration/profile.html", {'form': form, 'password_from': pasw})
    return redirect('contact_list')
