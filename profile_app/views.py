from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
##########
# from profile_app.forms import *
from profile_app.models import *
##########
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.defaults import page_not_found
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail,BadHeaderError
import random

# Create your views here.
def index(request):
	return render(request,'inicio.html')