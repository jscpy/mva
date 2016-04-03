from django.contrib import auth
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import FormView, TemplateView, RedirectView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from mva.forms import UserForm, UserLoginForm

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
	form_class = UserForm
	success_url = '/success/submit/'

	def form_valid(self, form):
		auth.models.User.objects.create_user(username = form.cleaned_data['username'],
		password = form.cleaned_data['password1']).save()
		print(self.request.POST['username'], self.request.POST['password1'])

		return super(RegisterForm, self).form_valid(form)

class UserSubmit(TemplateView):
	template_name = "success_submit.html"