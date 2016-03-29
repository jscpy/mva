from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

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

SESSION_STATUS = (
	('a','Approved'),
	('s','Submited'),
	('r','Rejected'),
)

class Session(models.Model):
	title = models.CharField(max_length=50)
	abstract = models.TextField(max_length=2000)
	track = models.ForeignKey(Track)
	speaker = models.ForeignKey(Speaker)
	status = models.CharField(max_length=1, choices=SESSION_STATUS)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('session_detail',kwargs={'pk':self.pk})
