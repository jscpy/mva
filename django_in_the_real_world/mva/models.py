from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

SESSION_STATUS = (
	('a','Approved'),
	('s','Submited'),
	('r','Rejected'),
)

SALONES = (
	('Salón Jupiter','Salón Jupiter'),
	('Salón Marte','Salón Marte'),
	('Salón Tierra','Salón Tierra'),
	('Salón Venus','Salón Venus')
)

class Speaker(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=50)
    bio = models.TextField(max_length=1000)
    twitter = models.CharField(max_length=16, blank=True)
    facebook = models.CharField(max_length=50, blank=True)

    def __str__(self):
    	return self.name


class Track(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField(max_length=1000)

	def __str__(self):
		return self.title


class Session(models.Model):
	title = models.CharField(max_length=50)
	abstract = models.TextField(max_length=1000)
	track = models.ForeignKey(Track)
	speaker = models.ForeignKey(Speaker)
	status = models.CharField(max_length=1, choices=SESSION_STATUS)
	salon = models.CharField(max_length=20, choices=SALONES, blank=True)
	date = models.DateField(blank=True)
	places = models.PositiveSmallIntegerField(default=200)
	places_off = models.PositiveSmallIntegerField(default=0)

	def __str__(self):
		return "{}".format(self.title)

	def get_absolute_url(self):
		return reverse('session_detail',kwargs={'pk':self.pk})

	def status_places(self):
		if self.places_off == 200:
			return "Lo sentimos pero ya no hay lugares para esta conferencia"
		else:
			return "Todavia tienes tiempo quedan {} lugares".format(self.places-self.places_off)

class Reservation(models.Model):
	session = models.ForeignKey(Session, related_name='session_reserved')
	person = models.ForeignKey(User, related_name='user_place')
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return "{}".format(self.session)

	class Meta:
		ordering = ('person',)
		unique_together = ('session', 'person')