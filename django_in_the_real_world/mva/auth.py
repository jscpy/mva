from django.contrib import auth
from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView

from mva.forms import UserForm

@auth.decorators.login_required
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
					next = '/sessions/'

				return redirect(next)

			else:
				return render(request, 'login.html', {"mensaje" : "Tu cuenta esta deshabilitada"})
		else:	
			return render(request, 'login.html',{"mensaje" : "Usuario incorrecto"})

class RegisterForm(FormView):
	template_name = 'user_form.html'
	form_class = UserForm
	success_url = '/success/submit/'

	def form_valid(self, form):
		auth.models.User.objects.create_user(username = form.cleaned_data['username'],
		password = form.cleaned_data['password1']).save()
		print(self.request.POST['username'], self.request.POST['password1'])

		return super(RegisterForm, self).form_valid(form)


class UserSubmit(TemplateView):
	template_name = "success_submit.html"