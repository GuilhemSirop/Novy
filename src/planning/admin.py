from django.contrib import admin

from .models import Inscription, ConnexionUser
from .forms import InscriptionForm, FormIdentification

class InscriptionAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	form = InscriptionForm
	#class Meta : 
		#model = Inscription
		#Permet de customiser l'administration

class FormIdentificationNovy(admin.ModelAdmin):
	list_display = ['user_pseudo', 'user_pass']
	form = FormIdentification

admin.site.register(Inscription, InscriptionAdmin)
admin.site.register(ConnexionUser, FormIdentificationNovy)

