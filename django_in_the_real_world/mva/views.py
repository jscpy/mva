from django.shortcuts import render
from django.views.generic import *
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from mva.models import Session
from mva.forms import SessionForm

class Index(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		context['saludo'] = 'Hola'
		context['mensaje'] = 'Mundo'

		return context

class SessionListView(LoginRequiredMixin, ListView):
	model = Session
	template_name = "session_list.html"
	context_object_name = 'sesiones'

class SessionDetailView(LoginRequiredMixin, DetailView):
	model = Session
	template_name = "session_detail.html"

class SessionCreateView(LoginRequiredMixin, CreateView, ):
	model = Session
	template_name = "session_form.html"
	form_class = SessionForm

class SessionUpdateView(LoginRequiredMixin, UpdateView, ):
	model = Session
	template_name = "session_form.html"
	form_class = SessionForm

class SessionDeleteView(LoginRequiredMixin, DeleteView, ):
	model = Session
	success_url = reverse_lazy('session_list')
