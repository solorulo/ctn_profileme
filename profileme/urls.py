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
	# Examples:
	# url(r'^$', profile_app.views.Index.as_view(), name='index'),
	# url(r'^trabajos/$', profile_app.views.Jobs.as_view(), name='jobs'),
	# url(r'^login/?$', 'profile_app.views.oauth_login'),
	# url(r'^logout/?$', 'profile_app.views.oauth_logout'),
	# url(r'^registro/?$', 'profile_app.views.register'),

	url(r'^login/?$', 'profile_app.views.oauth_login'),
	url(r'^logout/?$', 'profile_app.views.oauth_logout'),
	url(r'^login/authenticated/?$', 'profile_app.views.oauth_authenticated'),
	url(r'^$','profile_app.views.home'),

	# url(r'^profileme/', include('profileme.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
)
