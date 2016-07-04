from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (View, TemplateView, DetailView, CreateView, 
UpdateView, ListView, DeleteView)

from .models import Session, Speaker, Reservation
from .forms import SessionForm, ReservationForm

class Index(TemplateView):
	template_name = "index.html"


class SessionListView(LoginRequiredMixin, ListView):
	model = Session
	template_name = "session_list.html"
	context_object_name = 'sesiones'


class SessionDetailView(LoginRequiredMixin, DetailView):
	model = Session
	template_name = "session_detail.html"


class SessionCreateView(LoginRequiredMixin, CreateView):
	model = Session
	template_name = "session_form.html"
	form_class = SessionForm

	def form_valid(self, form):
		mensaje = "Se ha creado '{}' correctamente".format(form.cleaned_data['title'])
		messages.success(self.request, mensaje)
		return super(SessionCreateView, self).form_valid(form)


class SessionUpdateView(LoginRequiredMixin, UpdateView):
	model = Session
	template_name = "session_form.html"
	form_class = SessionForm

	def form_valid(self, form):
		mensaje = "Se ha actualizado '{}' correctamente".format(form.cleaned_data['title'])
		messages.info(self.request, mensaje)
		return super(SessionUpdateView, self).form_valid(form)


class SessionDeleteView(LoginRequiredMixin, DeleteView):
	model = Session
	template_name = "session_confirm_delete.html"
	success_url = reverse_lazy('session_list')

	def delete(self, request, *args, **kwargs):
		mensaje = "El registro se ha eliminado correctamente"
		messages.error(self.request, mensaje)
		return super(SessionDeleteView, self).delete(request, *args, **kwargs)


class SpeakerDetailView(LoginRequiredMixin, DetailView):
	model = Speaker
	template_name = "speaker_detail.html"


class ReservationView(LoginRequiredMixin, CreateView):
	model = Reservation
	template_name = 'reservation_form.html'
	form_class = ReservationForm

	def form_valid(self, form):
		from django.db.utils import IntegrityError

		session = form.cleaned_data['session']
		user = self.request.user
		contador = Reservation.objects.filter(person = user).count()
		
		if contador == 3:
			messages.error(self.request, "Lo sentimos, ya te haz registrado a 3 conferencias")
			next = "reservation_list"
		else:
			reservacion = Reservation(session = session, person = user)
			try:
				reservacion.save()
			except IntegrityError as e:
				messages.error(self.request, "Ya te haz registrado para esta conferencia")
				next = 'reservation_create'
			else:
				sesion = Session.objects.get(title = session)
				sesion.places_off += 1
				sesion.save()
				messages.success(self.request, "Tu registro se realizo con exito")
				next = 'session_list'
		
		return redirect(reverse_lazy(next))


class ReservationListView(LoginRequiredMixin, ListView):
    template_name = "reservation_list.html"
    context_object_name = 'reservaciones'

    def get_queryset(self):
    	self.reservation = Reservation.objects.filter(person = self.request.user)
    	return self.reservation


class PasesView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		from django.template import Template, Context
		from weasyprint import HTML, CSS

		with open('templates/pases.html','r') as t:
			html_template = Template(t.read())

		reservaciones = Reservation.objects.filter(person = request.user)

		c = Context({
				'usuario' : request.user,
				'reservaciones' : reservaciones
			})

		rendered_html = html_template.render(c)

		pdf_file = HTML(string=rendered_html, encoding="UTF-8", base_url=request.build_absolute_uri()).write_pdf()
		response = HttpResponse(pdf_file, content_type='application/pdf')
		response['Content-Disposition'] = 'inline; filename="pases.pdf"'
		return response