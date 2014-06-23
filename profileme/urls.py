from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
import profile_app.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# importamos settings
from profileme import settings

urlpatterns = patterns('',
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	
	url(r'^logout/?$', 'profile_app.views.oauth_logout'),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('profile_app.views',
	url(r'^$','index'),

	url(r'^profile$', 'profile', name='profile'),
	url(r'^jobs$', 'jobs', name='jobs'),

    url(r'^postTest$', 'postTest', name='postTest'),
    url(r'^registerUser$', 'registerUser', name='registerUser'),
    url(r'^createJobOffer$', 'createJobOffer', name='createJobOffer'),
    url(r'^registro$', 'registro', name='registro'),

    url(r'^registerUser$', 'registerUser', name='registerUser'),
    url(r'^uploadUserPhoto$', 'uploadUserPhoto', name='uploadUserPhoto'),

    url(r'^publicar_oferta$', 'publicarOferta', name='publicarOferta'),
    # url(r'^publicarOferta$', 'profile_app.views.publicarOferta', name='publicarOferta'),
    
    url(r'^createJobOffer$', 'createJobOffer', name='createJobOffer'),
)

urlpatterns += patterns('profile_app.linkedin_views',
	url(r'^login/linkedin/?$', 'oauth_login'),
	url(r'^login/linkedin/authenticated/?$', 'oauth_authenticated'),
)
