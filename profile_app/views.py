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
			company = Company.objects.get(email=email)
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
		empresa = Empresa.objects.get(email=email)
	except Exception, e:
		return render(request, 'simple_post_response.html', {'response_message':'error al obtener empresa'})

	# TODO: Check for valid and complete info
	# if puesto="" or  

	jobOffer = Trabajo.objects.create(empresa=empresa, puesto=name, genero=gender, edad=age, experiencia=experience, escolaridad=schoolLevel,
							habilidades=skills, descripcion=description, sueldo=compensation)

	jobOffer.save();

	return render(request, 'simple_post_response.html', {'response_message':'ok'})
