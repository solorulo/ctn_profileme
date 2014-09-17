# Django settings for profileme project.
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEBUG = True

TEMPLATE_DEBUG = DEBUG

LOGIN_URL='/'

LINKEDIN_TOKEN='75jjffqcztuv6i'
LINKEDIN_SECRET='6ouOGh6oozhhEB8g'
# Add email to requested authorizations.
LINKEDIN_SCOPE = ['r_fullprofile', 'r_emailaddress', 'r_contactinfo']
# Add the fields so they will be requested from linkedin.
LINKEDIN_EXTRA_FIELD_SELECTORS = ['email-address', 'headline', 'industry', 'skills', 'courses', 'phone-numbers']
# Arrange to add the fields to UserSocialAuth.extra_data
LINKEDIN_EXTRA_DATA = [('id', 'id'),
					   ('first-name', 'first_name'),
					   ('last-name', 'last_name'),
					   ('email-address', 'email_address'),
					   ('headline', 'headline'),
					   ('industry', 'industry'),
					   ('skills', 'skills'),
					   ('courses', 'courses'),
					   ('phone-numbers', 'phone-numbers') ]

LOCAL_DEV = False

if LOCAL_DEV :
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
	        'NAME': 'profileme.db',                      # Or path to database file if using sqlite3.
	        # The following settings are not used with sqlite3:
	        'USER': '',
	        'PASSWORD': '',
	        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
	        'PORT': '',                      # Set to empty string for default.
	    }
	}
else :
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
	        'NAME': 'd1oi983566bgig',                      # Or path to database file if using sqlite3.
	        # The following settings are not used with sqlite3:
	        'USER': 'fyftokdfbgpnwd',
	        'PASSWORD': 'LVpti1WINBgcT71SMutscLA-md',
	        'HOST': 'ec2-54-197-241-79.compute-1.amazonaws.com',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
	        'PORT': '',                      # Set to empty string for default.
	    }
	}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'www.profileme.com.mx', 'profileme.com.mx', 'profileme.herokuapp.com']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Mexico_City'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-mx'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
ruta = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/media/'
MEDIA_ROOT = ruta

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_URL = '/static/'

STATIC_ROOT= os.path.join(BASE_DIR,'staticfiles/')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static/'),
)

# List of finder classes that know how to find static files in
# various locations.
# STATICFILES_FINDERS = (
# 	'django.contrib.staticfiles.finders.FileSystemFinder',
# 	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
# )

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'fq=#o618#koqnmdkbrb^ziet_3df-mu*qzum*uu3^2pz!dv)^x'

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	# Uncomment the next line for simple clickjacking protection:
	# 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'profileme.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'profileme.wsgi.application'

AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_DIRS = (
	# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
	'templates'
)

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'profile_app',
	# Uncomment the next line to enable the admin:
	'django.contrib.admin',
	# Uncomment the next line to enable admin documentation:
	# 'django.contrib.admindocs',
)
