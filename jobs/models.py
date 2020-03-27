  
from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=140, default='title')
    host = models.CharField(max_length=140, default='host')
    used_tech = models.CharField(max_length=140, default='Skils')
    link = models.CharField(max_length=140, default='link')
    summary = models.TextField(max_length=400)


class Contact(models.Model):
	serial = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	email = models.EmailField(max_length = 254)
	message = models.TextField(max_length=400)
	date = models.DateTimeField(auto_now_add=True, blank=True)
