from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from mva.forms import UserForm


class UserCreateView(CreateView):
    model = User
    template_name = "user_form.html"
    form_class = UserForm
    succes_url = ('session_list')

def logout(request):
	auth.logout(request)
	return redirect('/')

def login(request):
	if request.method == 'GET':
		return render(request, 'login.html')
	
	elif request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username = username, password = password)

		if user is not None:
			if user.is_active:
				auth.login(request, user)
				next = ''
				if 'next' in request.GET:
					next = request.GET['next']
				if next == None or next == '':
					next = '/sessions'

				return redirect(next)

			else:
				return render(request, 'login.html', {"mensaje" : "Tu cuenta esta deshabilitada"})
		else:	
			return render(request, 'login.html',{"mensaje" : "Usuario incorrecto"})
