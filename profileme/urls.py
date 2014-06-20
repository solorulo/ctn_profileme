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

urlpatterns += patterns('',
    url(r'^$', 'profile_app.views.index', name='index'),

    url(r'^postTest$', 'profile_app.views.postTest', name='postTest'),

    url(r'^registro$', 'profile_app.views.registro', name='registro'),

    url(r'^registerUser$', 'profile_app.views.registerUser', name='registerUser'),
    url(r'^uploadUserPhoto$', 'profile_app.views.uploadUserPhoto', name='uploadUserPhoto'),

    url(r'^publicar_oferta$', 'profile_app.views.publicarOferta', name='publicarOferta'),
    # url(r'^publicarOferta$', 'profile_app.views.publicarOferta', name='publicarOferta'),
    url(r'^createJobOffer$', 'profile_app.views.createJobOffer', name='createJobOffer'),
)

urlpatterns += patterns('profile_app.linkedin_views',
	url(r'^login/linkedin/?$', 'oauth_login'),
	url(r'^login/linkedin/authenticated/?$', 'oauth_authenticated'),
)
