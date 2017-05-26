from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Staff (models.Model):
	username = models.CharField(max_length=100, null=True)
	full_name = models.CharField(max_length=100, null=True)	
	role = models.CharField(max_length=20, null=True)	
	photo = models.ImageField(upload_to='staffs', blank=True)

	def __str__(self):
		return self.full_name

class Akun_Staff (models.Model):
	JENIS_AKUN_CHOICES = (		
		('admin', 'Admin'),
		('surveyer', 'Surveyer'),
		('quality', 'Quality'),
	)
	akun = models.ForeignKey(User)	
	staff = models.ForeignKey(Staff)
	jenis_akun = models.CharField(max_length=10, choices=JENIS_AKUN_CHOICES)
	
	def __str__(self):
		return self.staff.full_name