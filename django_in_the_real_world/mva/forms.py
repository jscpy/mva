from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

from mva.models import Session

class SessionForm(forms.ModelForm):
	class Meta:
		model = Session
		fields = ['title','abstract','track','speaker']

	def __init__(self, *args, **kwargs):
		super(SessionForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_class = 'form-horizontal'
		self.helper.field_classs = 'col-md-4'
		self.helper.add_input(Submit('submit','Save'))

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','password1',]

	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_class = 'form-horizontal'
		self.helper.field_classs = 'col-md-4'
		self.helper.add_input(Submit('submit','Enviar'))

class UserLoginForm(AuthenticationForm):
	class Meta:
		model = User
		fields = ['username','password']

	def __init__(self, *args, **kwargs):
		super(UserLoginForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_class = 'form-horizontal'
		self.helper.field_classs = 'col-md-4'
		self.helper.add_input(Submit('submit','Entrar'))