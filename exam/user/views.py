from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from user.forms import RegistrationForm
from user.models import User
from django.contrib.auth.forms import AuthenticationForm


