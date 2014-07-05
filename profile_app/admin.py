from profile_app.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton
# class UserProfileInline(admin.StackedInline):
#     model = PersonalData
#     can_delete = False
#     verbose_name_plural = 'perfiles'

# # Define a new User admin
# class UserAdmin(UserAdmin):
#     inlines = (UserProfileInline, )

# Re-register UserAdmin

admin.site.unregister(Group)
admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
admin.site.register(PersonalData)
admin.site.register(Proyecto)

admin.site.register(Habilidad)
admin.site.register(Herramienta)
admin.site.register(Hobbie)

admin.site.register(Educacion)

admin.site.register(Company)
admin.site.register(Trabajo)

admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Ciudad)
