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

class CampoTrabajo(models.Model):
	nombre = models.CharField(max_length=50)

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

class Trabajo(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=400)
	puesto = models.CharField(max_length=400)

	def __unicode__(self):
		return self.nombre	

class Educacion(models.Model):
	centroEstudios = models.ForeignKey(CentroEstudios)
	titulo = models.ForeignKey(Titulo)
	persona = models.ForeignKey(User)

class Hobbie(models.Model):
	"""docstring for Hobbie"""
	def __init__(self, arg):
		super(Hobbie, self).__init__()
		self.arg = arg
	
	nombre = models.CharField(max_length=100)
	foto = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre	

# Create your models here.
class PersonalData(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	telefono = models.CharField(max_length=15,null=True,blank=True)
	certificaciones = models.CharField(max_length=400,null=True,blank=True)
	camposTrabajo = models.ManyToManyField(CampoTrabajo,null=True,blank=True)
	img = models.CharField(max_length=100,null=True,blank=True)
	hobbies = models.CharField(max_length=200,null=True,blank=True)
	idiomas = models.ManyToManyField(Idioma,null=True,blank=True)

	oauth_token = models.CharField(max_length=200)
	oauth_secret = models.CharField(max_length=200)

	def __unicode__(self):
		return self.user.username

		