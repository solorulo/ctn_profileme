# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Pais(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

class Estado(models.Model):
	nombre = models.CharField(max_length=50)
	pais = models.ForeignKey(Pais)

	def __unicode__(self):
		return self.nombre

class Ciudad(models.Model):
	nombre = models.CharField(max_length=50)
	estado = models.ForeignKey(Estado)

	def __unicode__(self):
		return self.nombre

# Company model
class Company(models.Model):
	usuario = models.OneToOneField(User)
	nombre = models.TextField(max_length=100)
	direccion = models.TextField(max_length=150)
	telefono = models.TextField(max_length=20)
	reclutador = models.TextField(max_length=100)

class Trabajo(models.Model):
	"""docstring for Trabajo"""
	# def __init__(self, arg):
	# 	super(Trabajo, self).__init__()
	# 	self.arg = arg
	empresa = models.ForeignKey(Company)

	puesto = models.CharField(max_length=100)
	genero = models.CharField(max_length=10)
	edad = models.CharField(max_length=3)
	experiencia = models.CharField(max_length=20)
	escolaridad = models.CharField(max_length=50)
	#
	habilidades = models.TextField(max_length=400)
	descripcion = models.TextField(max_length=400)
	sueldo = models.CharField(max_length=100)

	def __unicode__(self):
		return self.puesto

class Educacion(models.Model):
	NONE = 0
	DOCTORADO = 1
	INGENIERIA = 2
	LICENCIATURA = 3
	PREPARATORIA = 4
	# USUARIO = 2
	TIPO_CHOICES = (
		(NONE, "Escolaridad"),
		(DOCTORADO, "Doctorado"),
		(INGENIERIA, "Ingeniería"),
		(LICENCIATURA, "Licenciatura"),
		(PREPARATORIA, "Preparatoria"),
		# (USUARIO, "Usuario"),
	)
	escolaridad = models.IntegerField(choices=TIPO_CHOICES, default=NONE)
	carrera = models.CharField(max_length=400,null=True,blank=True)

class Hobbie(models.Model):	
	nombre = models.CharField(max_length=100)
	foto = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre	

# Create your models here.
class PersonalData(User):
	"""docstring for PersonalData"""
	# def __init__(self, arg):
	# 	super(PersonalData, self).__init__()
	# 	self.arg = arg
	birthday = models.DateField(null=True,blank=True)
	profesion = models.CharField(max_length=140,null=True,blank=True)
	telefono = models.CharField(max_length=15,null=True,blank=True)
	ciudad = models.ForeignKey(Ciudad,null=True,blank=True)
	trabajo = models.CharField(max_length=140,null=True,blank=True)
	educacion = models.ForeignKey(Educacion,null=True,blank=True)

	certificaciones = models.CharField(max_length=400,null=True,blank=True)
	img = models.CharField(max_length=100,null=True,blank=True)
	hobbies = models.ManyToMany(Hobbie,null=True,blank=True)

	oauth_token = models.CharField(max_length=200,null=True,blank=True)
	oauth_secret = models.CharField(max_length=200,null=True,blank=True)

	def __unicode__(self):
		return self.username

	class Meta:
		db_table = 'personal_data'

	def age(self):
		import datetime
		return int((datetime.date.today() - self.birthday).days / 365.25  )

class Habilidad(models.Model):
	user = models.ForeignKey(PersonalData)
	nombre = models.CharField(max_length=100)
	puntos = models.IntegerField()

	def __unicode__(self):
		return self.nombre

class Herramienta(models.Model):
	user = models.ForeignKey(PersonalData)
	nombre = models.CharField(max_length=100)
	puntos = models.IntegerField()

	def __unicode__(self):
		return self.nombre

class Proyecto(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=200)
	url = models.CharField(max_length=100)
	persona = models.ForeignKey(PersonalData)
