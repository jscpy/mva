from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib import auth

from mva.models import Session
from mva.forms import SessionForm

class Index(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		context['saludo'] = 'Hola'
		context['mensaje'] = 'Mundo'

		return context

class SessionListView(auth.mixins.LoginRequiredMixin, ListView):
	model = Session
	template_name = "session_list.html"
	context_object_name = 'sesiones'

class SessionDetailView(auth.mixins.LoginRequiredMixin, DetailView):
	model = Session
	template_name = "session_detail.html"

class SessionCreateView(auth.mixins.LoginRequiredMixin, CreateView, ):
	model = Session
	template_name = "session_form.html"
	form_class = SessionForm

class SessionUpdateView(auth.mixins.LoginRequiredMixin, UpdateView, ):
	model = Session
	template_name = "session_form.html"
	form_class = SessionForm

class SessionDeleteView(auth.mixins.LoginRequiredMixin, DeleteView, ):
	model = Session
	success_url = reverse_lazy('session_list')
