from django.views.generic import FormView, TemplateView, RedirectView, View
from django.shortcuts import render, redirect, render_to_response
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin

from mva.forms import UserCreateForm, UserLoginForm

class LogoutView(LoginRequiredMixin, RedirectView):
	pattern_name = 'login'

	def get(self, request, *args, **kwargs):
		auth.logout(request)
		return super(LogoutView, self).get(request, *args, **kwargs)

class LoginView(View):
	template_name = 'login.html'
	form_class = UserLoginForm

	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'form':form})

	def post(self, request, *args, **kwargs):
		form = self.form_class()

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
				return render(request, 'login.html', {"mensaje" : "Tu cuenta esta deshabilitada","form":form})
		else:
			return render(request, 'login.html', {"mensaje" : "Usuario incorrecto","form":form})

class RegisterForm(FormView):
	template_name = 'user_form.html'
	form_class = UserCreateForm
	success_url = '/sessions/'
	#succes_url = '/success/submit/'

	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password1']

		auth.models.User.objects.create_user(username = username, password = password).save()

		user = auth.authenticate(username = username, password = password)

		auth.login(self.request, user)

		return super(RegisterForm, self).form_valid(form)

# Si se desea redirigir a un mensaje de registro exitoso
# se debe cambiar el success_url de RegisterForm
class UserSubmit(TemplateView):
	template_name = "success_submit.html"
