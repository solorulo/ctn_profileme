##########
# from profile_app.forms import *
from profile_app.forms import UploadFileForm
from profile_app.models import *
##########
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.views.defaults import page_not_found
from django.views.generic import View
import cgi
import datetime
import json
import oauth2 as oauth
import random
import re

# /logout (requires login)
@login_required
def oauth_logout(request):
	# Log a user out using Django's logout function and redirect them
	# back to the homepage.
	auth_logout(request)
	return HttpResponseRedirect('/')

# / (requires login)
# @login_required
# def home(request):
# 	html = "<html><body>"
# 	# token = oauth.Token(request.user.get_profile().oauth_token,request.user.get_profile().oauth_secret)
# 	# client = oauth.Client(consumer,token)
# 	# headers = {'x-li-format':'json'}
# 	# url = "http://api.linkedin.com/v1/people/~:(id,first-name,last-name,headline)"
# 	# resp, content = client.request(url, "GET", headers=headers)
# 	# profile = json.loads(content)
# 	# html += profile['firstName'] + " " + profile['lastName'] + "<br/>" + profile['headline']
# 	user = request.user
# 	html += user.first_name + " " + user.last_name + "<br/>" + user.email
# 	return HttpResponse(html)

@login_required
def profile (request):
	return render(request,'perfil.html')

# Create your views here.
def index(request):
	#return HttpResponse("Inicio")
	if (request.user.is_authenticated()) :
		return redirect('profile')
	if request.method == 'POST':
		try:
			username = request.POST['user']
			password = request.POST['pass']
			user = authenticate(username=username, password=password)
			if not user:
				return render(request,'inicio.html', {'incorrect_password':True})
			auth_login(request, user)
			return redirect('profile')
		except:
			pass
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

	user = PersonalData(
			first_name=request.POST['name'] + ' ' + request.POST['lastname'],
			username=request.POST['email'],
			email=request.POST['email'],
			telefono='545678',
			certificaciones='no se que esta pasando')
	user.set_password(request.POST['password'])

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
@login_required
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

# 
def companyLogin(request):
	if request.method == "POST":
		companyName = request.POST["name"].strip()
		companyEmail = request.POST["email"].strip()

		if companyName == "" or companyEmail == "":
			return render(request, 'simple_post_response.html', {'response_message': 'incomplete_data'})

		# TODO: Change for a manual get or create to verify againts only relevant data fields
		# company, created = Company.objects.get_or_create(name=companyName, email=companyEmail)

	return render(request, 'simple_post_response.html', {'response_message': 'ok'})

def publicarOferta(request):
	responseParams = None

	if request.method == "POST":
		name = request.POST["companyName"].strip()
		email = request.POST["companyEmail"].strip()

		if name == "" or email == "":
			return render(request, 'simple_post_response.html', {'response_message': 'incomplete_data'})

		company = None
		try:
			company = User.objects.get(email=email)
		except Exception, e:
			user = User.objects.create_user(email, email)
			user.save()

			company = Company.objects.create(usuario=user, nombre=name)
			company.save()

			responseParams = {"company":company}

	return render(request, 'Empleados.html', responseParams)

# def publicarOferta(request):
# 	return render(request, 'Empleados.html', responseParams)

# Create Job Offer
def createJobOffer(request):
	response = ""

	for v in request.POST:
		response = response + v + ": " + request.POST[v] + "\n"

	context = {
		'response_message':response
	}

	name = request.POST.get("name").strip()
	compensation = request.POST.get("compensation").strip()
	skills = request.POST.get("skills").strip()
	age = request.POST.get("age").strip()
	telephone = request.POST.get("telephone").strip()
	experience = request.POST.get("experience").strip()
	state = request.POST.get("state").strip()
	address = request.POST.get("address").strip()
	schoolLevel = request.POST.get("schoolLevel").strip()
	recruiterName = request.POST.get("recruiterName").strip()
	email = request.POST.get("email").strip()
	description = request.POST.get("description").strip()
	position = request.POST.get("position").strip()
	gender = request.POST.get("gender").strip()

	empresa = None
	try:
		empresa = User.objects.get(email=email).company
		# return render(request, 'simple_post_response.html', {'response_message':'empresa encontrada'})
	except Exception, e:
		return render(request, 'simple_post_response.html', {'response_message':'error al obtener empresa'})

	# TODO: Check for valid and complete info
	# if puesto="" or  

	jobOffer = Trabajo.objects.create(empresa=empresa, puesto=name, genero=gender, edad=age, experiencia=experience, escolaridad=schoolLevel,
							habilidades=skills, descripcion=description, sueldo=compensation)

	jobOffer.save();

	return render(request, 'simple_post_response.html', {'response_message':'ok'})

def ofertas(request):
	return render(request, 'trabajos.html')