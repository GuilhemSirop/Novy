from django import forms

from .models import Inscription, ConnexionUser

class InscriptionForm(forms.ModelForm):
	class Meta:
		model = Inscription
		fields = ['full_name', 'email'] #champs de Inscription
	
	def clean_email(self): #overwriting function for cleaning email data, self est l'instance du formulaire
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		if not domain == 'novy':
			raise forms.ValidationError("Vous devez appartenir au domaine novy pour vous inscrire")
		if not extension == "fr":
			raise forms.ValidationError("Veuillez utiliser une adresse mail française !")
		return email 

	def clean_full_name(self): #overwriting function for cleaning email data, self est l'instance du formulaire
		full_name = self.cleaned_data.get('full_name')
		#verifications ? 
		return full_name

class FormIdentification(forms.ModelForm):
	class Meta:
		model = ConnexionUser
		fields = ['user_pseudo','user_pass']
		

		def clean_user_pseudo(self): #overwriting function for cleaning email data, self est l'instance du formulaire
			user_pseudo = self.cleaned_data.get('user_pseudo')
			email_base, provider = email.split("@")
			domain, extension = provider.split('.')
			if not domain == 'novy':
				raise forms.ValidationError("Vous devez appartenir au domaine novy pour vous inscrire")
			if not extension == "fr":
				raise forms.ValidationError("Veuillez utiliser une adresse mail française !")
			return user_pseudo

		def clean_user_pass(self): #overwriting function for cleaning email data, self est l'instance du formulaire
			user_pass = self.cleaned_data.get('user_pass')
			#verifications ? 
			return user_pass