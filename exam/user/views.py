from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from user.forms import RegistrationForm
from user.models import User
from django.contrib.auth.forms import AuthenticationForm


def user_registration(request):
    registration_form = RegistrationForm()
    if request.method == 'POST':
        print(request.POST)
        registration_form: RegistrationForm = RegistrationForm(request.POST)
        print(registration_form.errors)
        if registration_form.is_valid():
            registration_form.save()
            return redirect('user:user_login')
    return render(request, template_name='user/registration.html', context={
        'form': registration_form
    })


def user_login(request):
    if request.user.is_authenticated:
        return redirect('ecommerce:orders')
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('ecommerce:orders')
    return render(request, template_name="user/login.html", context={
        'form': form
    })


def user_logout(request, *args, **kwargs):
    logout(request)
    return redirect('user:user_login')
