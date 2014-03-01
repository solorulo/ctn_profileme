from django import forms
from django.forms import FileInput

class UploadFileForm(forms.Form):
	file  = forms.FileField()