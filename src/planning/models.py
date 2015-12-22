from django.db import models

# Create your models here.
class Inscription(models.Model):
	
	email = models.EmailField() #champ email prédéfini
	full_name = models.CharField(max_length = 200, default='', blank = True, null=True) #champ character, default, null et blank peuvent être utilisés par plusieurs champs models
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) #Moment de l'inscription, Date
	updated = models.DateTimeField(auto_now_add = False, auto_now=True)
	#auto_now_add : lorsque le modèle est crée
	#auto_now : lors d'une sauvegarde (inverse d'un update)
	
	def __unicode__(self):
		return self.email

class ConnexionUser(models.Model):

	user_pseudo = models.EmailField()
	user_pass = models.CharField(max_length = 50, default='', blank = True, null = True)

	def __unicode__(self):
		return self.user_pseudo
