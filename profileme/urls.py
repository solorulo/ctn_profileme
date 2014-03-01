from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.contrib.auth import views as auth_views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# importamos settings
from profileme import settings

urlpatterns = patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # Examples:
    url(r'^$', 'profile_app.views.index', name='index'),
    # url(r'^profileme/', include('profileme.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^postTest$', 'profile_app.views.postTest', name='postTest'),
    url(r'^registerUser$', 'profile_app.views.registerUser', name='registerUser'),
    url(r'^createJobOffer$', 'profile_app.views.createJobOffer', name='createJobOffer'),
    url(r'^registro$', 'profile_app.views.registro', name='registro'),

    url(r'^uploadUserPhoto$', 'profile_app.views.uploadUserPhoto', name='uploadUserPhoto'),    
)
