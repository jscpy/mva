from django import forms
from django.contrib.auth.models import User

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

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username','password',]

	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_class = 'form-inline'
		self.helper.field_classs = 'col-md-4'
		self.helper.add_input(Submit('submit','Enviar'))
	