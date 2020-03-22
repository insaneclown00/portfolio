  
from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=140, default='title')
    host = models.CharField(max_length=140, default='host')
    used_tech = models.CharField(max_length=140, default='Skils')
    summary = models.TextField(max_length=400)