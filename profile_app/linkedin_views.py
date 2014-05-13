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
import urllib

# from settings.py
consumer = oauth.Consumer(settings.LINKEDIN_TOKEN, settings.LINKEDIN_SECRET)
client = oauth.Client(consumer)
request_token_url = 'https://api.linkedin.com/uas/oauth/requestToken'
access_token_url = 'https://api.linkedin.com/uas/oauth/accessToken'
authenticate_url = 'https://www.linkedin.com/uas/oauth/authenticate'

def oauth_login(request):
	# Step 0. Get the current hostname and port for the callback
	if request.META['SERVER_PORT'] == 443:
		current_server = "https://" + request.META['HTTP_HOST']
	else:
		current_server = "http://" + request.META['HTTP_HOST']
		oauth_callback = current_server + "/login/linkedin/authenticated"
	# Step 1. Get a request token from Provider.
	resp, content = client.request("%s?oauth_callback=%s" % (request_token_url,oauth_callback), "GET")
	if resp['status'] != '200':
		raise Exception("Invalid response from Provider.")
	# Step 2. Store the request token in a session for later use.
	request.session['request_token'] = dict(cgi.parse_qsl(content))
	# Step 3. Redirect the user to the authentication URL.
	url = "%s?oauth_token=%s" % (authenticate_url,
		request.session['request_token']['oauth_token'])
	print url
	return HttpResponseRedirect(url)

# / (requires login)
# @login_required
# def home(request):
# 	html = "<html><body>"
# 	token = oauth.Token(request.user.get_profile().oauth_token,request.user.get_profile().oauth_secret)
# 	client = oauth.Client(consumer,token)
# 	headers = {'x-li-format':'json'}
# 	url = "http://api.linkedin.com/v1/people/~:(id,first-name,last-name,headline)"
# 	resp, content = client.request(url, "GET", headers=headers)
# 	profile = json.loads(content)
# 	html += profile['firstName'] + " " + profile['lastName'] + "<br/>" + profile['headline']
# 	return HttpResponse(html)

# /logout (requires login)
@login_required
def oauth_logout(request):
	# Log a user out using Django's logout function and redirect them
	# back to the homepage.
	auth_logout(request)
	return HttpResponseRedirect('/')

#/login/authenticated/
def oauth_authenticated(request):
	# Step 1. Use the request token in the session to build a new client.
	token = oauth.Token(request.session['request_token']['oauth_token'],
		request.session['request_token']['oauth_token_secret'])
	if 'oauth_verifier' in request.GET:
		token.set_verifier(request.GET['oauth_verifier'])
		client = oauth.Client(consumer, token)
	# Step 2. Request the authorized access token from Provider.
	resp, content = client.request(access_token_url, "GET")
	print 'status %s' % resp['status']
	if resp['status'] != '200':
		print content
		raise Exception("Invalid response from Provider.")
	access_token = dict(cgi.parse_qsl(content))
	headers = {'x-li-format':'json'}
	url = "http://api.linkedin.com/v1/people/~:(id,first-name,last-name,industry,email-address,courses,phone-numbers,picture-urls::(original))"
	token = oauth.Token(access_token['oauth_token'],
		access_token['oauth_token_secret'])
	client = oauth.Client(consumer,token)
	resp, content = client.request(url, "GET", headers=headers)
	print content
	profile = json.loads(content)  
	# Step 3. Lookup the user or create them if they don't exist.
	firstname = profile['firstName']
	lastname = profile['lastName']
	email = profile['emailAddress']
	identifier = profile['id']
	profesion = profile['industry']
	phoneNumbers = profile['phoneNumbers']
	phone = None
	if phoneNumbers['_total'] > 0 :
		phone = phoneNumbers['values'][0]['phoneNumber']
		print "phone : "+phone

	cursos = []
	if 'courses' in profile and profile['courses']['_total'] > 0:
		__cursos = profile['courses']['values']
		for curso in __cursos:
			cursos.append(curso['name'])
			print "curso : "+curso['name']

	if 'pictureUrls' in profile and profile['pictureUrls']['_total'] > 0:
		urlImg = profile['pictureUrls']['values'][0]
		urllib.urlretrieve (urlImg, '/Users/mkfnx/dev/ctn_profileme/media/' + identifier + ".jpg")
		# url2 = "http://api.linkedin.com/v1/people/~/picture-urls::(original)"
		# resp2, content2 = client.request(url, "GET", headers=headers)
		print 'url-img:'+urlImg
	
	try:
		user = User.objects.get(username=identifier)
		# Authenticate the user and log them in using Django's pre-built
		# functions for these things.
		user = authenticate(username=identifier,
			password=access_token['oauth_token_secret'])
		auth_login(request, user)
		return HttpResponseRedirect('/')
	except User.DoesNotExist:
		user = User.objects.create_user(identifier,
			email,
			access_token['oauth_token_secret'])                 
		user.first_name = firstname
		user.last_name = lastname
		user.save()
		# Save our permanent token and secret for later.
		userprofile = PersonalData(user=user,
			oauth_token=access_token['oauth_token'],
			oauth_secret=access_token['oauth_token_secret'])
		# userprofile.user = user
		# userprofile.oauth_token = access_token['oauth_token']
		# userprofile.oauth_secret = access_token['oauth_token_secret']
		userprofile.save()# Authenticate the user and log them in using Django's pre-built
		# functions for these things.
		user = authenticate(username=identifier,
			password=access_token['oauth_token_secret'])
		auth_login(request, user)
		return HttpResponseRedirect('/registro')
