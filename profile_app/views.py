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

from profile_app.forms import UploadFileForm

# Create your views here.
def index(request):
	#return HttpResponse("Inicio")
	return render(request,'inicio.html')

def registro(request):
	return render(request, 'Registro.html')

def postTest(request):
	return render(request, 'trabajos.html')

# Register User
def registerUser(request):
	if request.method != "POST":
		return render(request, 'simple_post_response.html', {'response_message': 'invalid_http_method'})

	name = request.POST['name'].strip()
	lastname = request.POST['lastname'].strip()
	username = request.POST['email'].strip()
	email = request.POST['email'].strip()
	password = request.POST['password'].strip()

	if name == "" or lastname == "" or username == "" or email == "" or password == "":
		return render(request, 'simple_post_response.html', {'response_message': 'incomplete_data'})

	if request.POST['email'] != request.POST['emailVerif']:
		return render(request, 'simple_post_response.html', {'response_message': 'email_missmatch'})

	user = User.objects.create_user(
			first_name=request.POST['name'],
			last_name=request.POST['lastname'],
			username=request.POST['email'],
			email=request.POST['email'],
			password=request.POST['password'])

	try:
		user.save()
	except IntegrityError as e:
		return render(request, 'simple_post_response', {'response_message': 'duplicated_user'})

	user = authenticate(username=request.POST['email'], password=request.POST['password'])
	if user == None:
		return render(request, 'simple_post_response.html', {'response_message': 'registration_error'})
	auth_login(request, user)

	return render(request, 'simple_post_response.html', {'response_message': 'ok'})

# Create Job Offer
def createJobOffer(request):

	context = {
	'response_message':':)'
	}

	return render(request, 'simple_post_response.html', context)

def uploadUserPhoto(request):
	file = None
	fName = None

	for f in request.FILES:
		fName = f

	file = request.FILES[fName]

	if file == None:
		return HttpResponseRedirect('/')

	with open('/Users/mkfnx/dev/ctn_profileme/media/' + file.name, 'wb+') as d:
		for c in file.chunks():
			d.write(c)

	response = "{'files': [{'name':'newFile.png','size': "+ str(file.size) +",'url': 'http://localhost:8000/media/" + file.name + "','thumbnailUrl':'','deleteUrl':'','deleteType': 'DELETE'}]}"

	pd = PersonalData.objects.create(user=request.user, img="/media/" + file.name)
	# pd.user = request.user
	# pd.img = "/media/" + file.name
	pd.save();

	return HttpResponse(response, content_type="application/json")
