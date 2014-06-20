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

class Proyecto(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=200)
	url = models.CharField(max_length=100)
	persona = models.ForeignKey(User)

class CentroEstudios(models.Model):
	nombre = models.CharField(max_length=50)
	logo = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class Titulo(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre	

class Idioma(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre	

class Habilidad(models.Model):
	nombre = models.CharField(max_length=100)
	puntos = models.IntegerField()

	def __unicode__(self):
		return self.nombre

class Herramienta(models.Model):
	nombre = models.CharField(max_length=100)
	puntos = models.IntegerField()

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
	def __init__(self, arg):
		super(Trabajo, self).__init__()
		self.arg = arg
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
		return self.nombre

class Educacion(models.Model):
	centroEstudios = models.ForeignKey(CentroEstudios)
	titulo = models.ForeignKey(Titulo)
	persona = models.ForeignKey(User)

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
	telefono = models.CharField(max_length=15,null=True,blank=True)
	certificaciones = models.CharField(max_length=400,null=True,blank=True)
	trabajo = models.CharField(max_length=140,null=True,blank=True)
	profesion = models.CharField(max_length=140,null=True,blank=True)
	img = models.CharField(max_length=100,null=True,blank=True)
	hobbies = models.CharField(max_length=200,null=True,blank=True)
	idiomas = models.ManyToManyField(Idioma,null=True,blank=True)
	ciudad = models.ForeignKey(Ciudad,null=True,blank=True)
	birthday = models.DateField(null=True,blank=True)

	oauth_token = models.CharField(max_length=200)
	oauth_secret = models.CharField(max_length=200)

	def __unicode__(self):
		return self.username

	class Meta:
		db_table = 'personal_data'

	def age(self):
		import datetime
		return int((datetime.date.today() - self.birthday).days / 365.25  )
