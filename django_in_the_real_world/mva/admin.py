from django.contrib import admin
from .models import *

# Register your models here.
class SpeakerAdmin(admin.ModelAdmin):
	list_display = ('name','bio')
	fieldsets = (
		('General Information', { 
			'fields' : ('name','bio','title')
		}),
		('Social media', {
			'classes' : ('collapse',), #Añadir coma al final 
			'fields' : ('twitter','facebook'),
			'description' : 'Add social media here'
		})
	)

class SessionAdmin(admin.ModelAdmin):
	search_fields = ['title','abstract']
	list_display = ('title','status')
	list_filter = ('track__title','speaker')
	actions = ['make_approved',]

	def make_approved(self, request, queryset):
		rows_updated = queryset.update(status = 'a')
		if rows_updated == 1:
			message_bit = '1 session was'
		else:
			message_bit = '{} sessions were'.format(rows_updated)

		self.message_user(request, '{} approved.'.format(message_bit))

	make_approved.short_description = 'Mark session(s) as approved'

class ReservationAdmin(admin.ModelAdmin):
	list_display = ('session','person')

admin.site.register(Track)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Session, SessionAdmin)