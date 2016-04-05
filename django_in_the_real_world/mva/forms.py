from django import forms
from django.contrib import auth

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from mva.models import Session

class SessionForm(forms.ModelForm):
	class Meta:
		model = Session
		fields = ['title','abstract','track','speaker']

	def __init__(self, *args, **kwargs):
		super(SessionForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.add_input(Submit('submit','Guardar'))

class UserCreateForm(auth.forms.UserCreationForm):
	class Meta:
		model = auth.models.User
		fields = ['username','password1',]

	def __init__(self, *args, **kwargs):
		super(UserCreateForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.add_input(Submit('submit','Enviar'))

class UserLoginForm(auth.forms.AuthenticationForm):
	class Meta:
		model = auth.models.User
		fields = ['username','password']

	def __init__(self, *args, **kwargs):
		super(UserLoginForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.add_input(Submit('submit','Entrar'))