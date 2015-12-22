from django.shortcuts import render
from .forms import InscriptionForm, FormIdentification
from .models import ConnexionUser

def home(request):
	title = "Planning novy"
	form = InscriptionForm(request.POST or None)
	welcome = "Bienvenue %s" %(request.user)

	context = {

		"planning_title" : title,
		"welcome_user": welcome,
		"form": form

	}

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		print(instance.email)
		print(instance.full_name)

		context = {

		"planning_title": "Merci de vous être enregistré"

		}
	else:
		print("error")

	return render(request, 'home.html', context)

def ConnexionNovy(request):

	titre_ConnexionNovy = "Bienvenue sur novy"
	form_connexion =  FormIdentification(request.POST or None)

	context = {

		"titre_page_connexion" : titre_ConnexionNovy,
		"form_connexion_render" : form_connexion

	}
	if form_connexion.is_valid():
		print("OKKKKK")

	return render(request, 'connexion.html', context)

def plan(request):
	return render(request, 'planning.html')
	

	

