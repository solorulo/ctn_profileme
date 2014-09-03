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
from django.utils import simplejson
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

@login_required
def profile (request):
	esc_opt = Educacion.TIPO_CHOICES
	# Carga herramientas
	db_herramientas = Herramienta.objects.filter(user=request.user.personaldata)
	herramientas = {
		'names' : [],
		'values' : []
	}
	if db_herramientas.count() > 0:
		for h in db_herramientas:
			herramientas['names'].append(str(h.nombre))
			herramientas['values'].append(h.puntos)
	# Carga habilidades
	db_habilidades = Habilidad.objects.filter(user=request.user.personaldata)
	habilidades = {
		'names' : [],
		'values' : []
	}
	if db_habilidades.count() > 0:
		for h in db_habilidades:
			habilidades['names'].append(str(h.nombre))
			habilidades['values'].append(h.puntos)
	# Carga proyectos
	db_proyectos = Proyecto.objects.filter(persona=request.user.personaldata)
	proyectos = []
	if db_proyectos.count() > 0:
		for h in db_proyectos:
			proyectos.append({
				'nombre':str(h.nombre),
				'descripcion':str(h.descripcion),
				'url':str(h.url),
			});
	# Carga hobbies
	usr_hobbies = {}
	for hb in request.user.personaldata.hobbies.all():
		usr_hobbies[hb.nombre] = True
	return render(request, 'perfil.html', { 
		'escolaridad' : esc_opt, 
		'hobbies' : simplejson.dumps(usr_hobbies), 
		'dbhobbies' : Hobbie.objects.all().values(), 
		'herramientas':herramientas, 
		'habilidades' : habilidades,
		'proyectos':proyectos
		})

# Create your views here.
def index(request):
	# usuario logueado
	if (request.user.is_authenticated()) :
		return redirect('profile')
	# login
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

def postTest(request):
	return render(request, 'trabajos.html')

@login_required
def registro(request):
	esc_opt = Educacion.TIPO_CHOICES
	hobbies = Hobbie.objects.all().values()
	db_herramientas = Herramienta.objects.filter(user=request.user.personaldata)
	db_habilidades = Habilidad.objects.filter(user=request.user.personaldata)
	herramientas = {
		'names' : [],
		'values' : []
	}
	if db_herramientas.count() > 0:
		for h in db_herramientas:
			herramientas['names'].append(str(h.nombre))
			herramientas['values'].append(h.puntos)
	habilidades = {
		'names' : [],
		'values' : []
	}
	if db_habilidades.count() > 0:
		for h in db_habilidades:
			habilidades['names'].append(str(h.nombre))
			habilidades['values'].append(h.puntos)
	print habilidades
	print herramientas
	return render(request, 'Registro.html', { 
		'escolaridad' : esc_opt, 
		'hobbies' : hobbies, 
		'herramientas':herramientas, 
		'habilidades' : habilidades  
		})

# Verificar que funcione bien
@login_required
def registrarHobbies(request):
	if request.method != "POST":
		return render(request, 'simple_post_response.html', {'response_message': 'invalid_http_method'})
	data = request.POST['data']
	obdata = simplejson.loads(data)
	all_hobbies = Hobbie.objects.all()
	last_objects = request.user.personaldata.hobbies
	print 'registrar hobbies'
	for ob in obdata:
		try:
			hob = all_hobbies.get(nombre=ob)
			request.user.personaldata.hobbies.add(hob)
			print ob
		except Exception, e:
			# raise e
			pass
	# last_objects.clear()
	return render(request, 'simple_post_response.html', {'response_message': 'ok'})

@login_required
def registrarHabilidades(request):
	if request.method != "POST":
		return render(request, 'simple_post_response.html', {'response_message': 'invalid_http_method'})
	data = request.POST['data']
	print data
	obdata = simplejson.loads(data)
	last_objects = Habilidad.objects.filter(user=request.user.personaldata)
	last_objects.delete()
	for ob in obdata:
		nhab = Habilidad.objects.create(
			user=request.user.personaldata,
			nombre=ob['nombre'],
			puntos=ob['puntos'])
		nhab.save()
	return render(request, 'simple_post_response.html', {'response_message': 'ok'})

@login_required
def registrarHerramientas(request):
	if request.method != "POST":
		return render(request, 'simple_post_response.html', {'response_message': 'invalid_http_method'})

	data = request.POST['data']

	# return render(request, 'simple_post_response.html', {'response_message': data})

	obdata = simplejson.loads(data)
	last_objects = Herramienta.objects.filter(user=request.user.personaldata)
	last_objects.delete()
	for ob in obdata:
		nhab = Herramienta.objects.create(
			user=request.user.personaldata,
			nombre=ob['nombre'],
			puntos=ob['puntos'])
		nhab.save()
	return render(request, 'simple_post_response.html', {'response_message': 'ok'})

@login_required
def registrarProyectos(request):
	if request.method != "POST":
		return render(request, 'simple_post_response.html', {'response_message': 'invalid_http_method'})
	data = request.POST['data']
	obdata = simplejson.loads(data)
	# print data
	print obdata
	last_objects = Proyecto.objects.filter(persona=request.user.personaldata)
	last_objects.delete()
	for ob in obdata:
		nhab = Proyecto.objects.create(
			persona=	request.user.personaldata,
			nombre=		ob['nombre'],
			descripcion=ob['descripcion'],
			url=		ob['url'])
		nhab.save()
	return render(request, 'simple_post_response.html', {'response_message': 'ok'})

@login_required
def registrarEscolaridad(request):
	if request.method != "POST":
		return render(request, 'simple_post_response.html', {'response_message': 'invalid_http_method'})

	escolaridad = int(request.POST.get('escolaridad', '0').strip())
	carrera = request.POST.get('carrera', '').strip()
	certificaciones = request.POST.get('certificaciones', '').strip()

	print escolaridad
	print certificaciones
	print carrera

	user = request.user

	if user.personaldata.educacion == None:
		educacion = Educacion.objects.create(escolaridad=escolaridad, carrera=carrera)
		user.personaldata.educacion = educacion
	else:
		educacion = user.personaldata.educacion
		educacion.escolaridad = escolaridad
		educacion.carrera = carrera
		
	user.personaldata.educacion.save()
	user.personaldata.certificaciones = certificaciones
	user.personaldata.save()
	user.save()

	return render(request, 'simple_post_response.html', {'response_message': 'ok'})


def jobs(request):
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
			telefono='',
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

@login_required
def uploadUserPhoto(request):
	file = None
	fName = None

	for f in request.FILES:
		fName = f

	file = request.FILES[fName]

	if file == None:
		return HttpResponseRedirect('/')

	from profileme.settings import MEDIA_ROOT
	print MEDIA_ROOT
	with open(MEDIA_ROOT+ "usrs/" + file.name, 'wb+') as d:
		for c in file.chunks():
			d.write(c)

	response = "{'files': [{'name':'newFile.png','size': "+ str(file.size) +",'url': 'http://127.0.0.1:8000/media/usrs/" + file.name + "','thumbnailUrl':'','deleteUrl':'','deleteType': 'DELETE'}]}"

	request.user.personaldata.img = "usrs/" + file.name
	# pd = PersonalData.objects.create(user=request.user, img="/media/" + file.name)
	# pd.user = request.user
	# pd.img = "/media/" + file.name
	request.user.personaldata.save();

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
			company = User.objects.get(email=email).company

			responseParams = {"company":company}
			# return render(request, 'simple_post_response.html', {'response_message': 'Ya estaba registrado ese correo'})
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
	jobOffers = Trabajo.objects.all()
	boxNum = ["2", "3"]

	return render(request, 'trabajos.html', {"jobOffers":jobOffers, "boxNum":boxNum})

def error_page(request):
	return render(request, 'error_page.html')

#
def updateUserBasicInfo(request):
	name = request.POST.get('name', '').strip()
	profesion = request.POST.get('profesion', '').strip()
	age = request.POST.get('age', '').strip()
	tel = request.POST.get('tel', '').strip()
	email = request.POST.get('email', '').strip()
	job = request.POST.get('job', '').strip()
	locality = request.POST.get('locality', '').strip()

	user = request.user

	user.first_name = name
	user.personaldata.profesion = profesion
	user.personaldata.age = age
	user.personaldata.telefono = tel
	user.email = email
	user.personaldata.trabajo = job

	if user.personaldata.ciudad == None:
		pais = Pais.objects.create(nombre=locality)
		estado = Estado.objects.create(nombre=locality, pais=pais)
		user.personaldata.ciudad = Ciudad.objects.create(nombre=locality, estado=estado)
	# else:
	# 	user.personaldata.ciudad.estado.pais = locality
	# 	user.personaldata.ciudad.estado = locality
	# 	user.personaldata.ciudad = locality

	success = True

	try:
		user.personaldata.save()
		user.save()
	except:
		success = False

	return render(request, 'simple_post_response.html', {'response_message':success})
