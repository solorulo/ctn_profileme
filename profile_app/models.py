from django.db import models
from django.contrib.auth.models import User


class Pais(models.Model):
	"""docstring for Pais"""
	def __init__(self, arg):
		super(Pais, self).__init__()
		self.arg = arg

	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

class Estado(models.Model):
	"""docstring for Estado"""
	def __init__(self, arg):
		super(Estado, self).__init__()
		self.arg = arg

	nombre = models.CharField(max_length=50)
	pais = models.ForeignKey(Pais)

	def __unicode__(self):
		return self.nombre

class Ciudad(models.Model):
	"""docstring for Ciudad"""
	def __init__(self, arg):
		super(Ciudad, self).__init__()
		self.arg = arg
	
	nombre = models.CharField(max_length=50)
	estado = models.ForeignKey(Estado)

	def __unicode__(self):
		return self.nombre

class CampoTrabajo(models.Model):
	"""docstring for CampoTrabajo"""
	def __init__(self, arg):
		super(CampoTrabajo, self).__init__()
		self.arg = arg

	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

class Proyecto(models.Model):
	"""docstring for Proyecto"""
	def __init__(self, arg):
		super(Proyecto, self).__init__()
		self.arg = arg

	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=200)
	url = models.CharField(max_length=100)
	persona = models.ForeignKey(User)

class CentroEstudios(models.Model):
	"""docstring for CentroEstudios"""
	def __init__(self, arg):
		super(CentroEstudios, self).__init__()
		self.arg = arg
	nombre = models.CharField(max_length=50)
	logo = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class Titulo(models.Model):
	"""docstring for Titulo"""
	def __init__(self, arg):
		super(Titulo, self).__init__()
		self.arg = arg
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre	

class Idioma(models.Model):
	"""docstring for Idioma"""
	def __init__(self, arg):
		super(Idioma, self).__init__()
		self.arg = arg
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre	

class Habilidad(models.Model):
	"""docstring for Habilidad"""
	def __init__(self, arg):
		super(Habilidad, self).__init__()
		self.arg = arg
	nombre = models.CharField(max_length=100)
	puntos = models.IntegerField()

	def __unicode__(self):
		return self.nombre

class Herramienta(models.Model):
	"""docstring for Herramienta"""
	def __init__(self, arg):
		super(Herramienta, self).__init__()
		self.arg = arg
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
	"""docstring for Educacion"""
	def __init__(self, arg):
		super(Educacion, self).__init__()
		self.arg = arg
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
	"""docstring for PersonalData"""
	# def __init__(self, arg):
	# 	super(PersonalData, self).__init__()
	# 	self.arg = arg
	user = models.OneToOneField(User, primary_key=True)
	telefono = models.CharField(max_length=15)
	certificaciones = models.CharField(max_length=400)
	camposTrabajo = models.ManyToManyField(CampoTrabajo)
	img = models.CharField(max_length=100)
	hobbies = models.CharField(max_length=200)
	idiomas = models.ManyToManyField(Idioma)

	def __unicode__(self):
		return self.user.username
