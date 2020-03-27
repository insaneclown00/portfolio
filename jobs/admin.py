from django.contrib import admin

# Register your models here.
from .models import Job, Contact

admin.site.register(Job)
admin.site.register(Contact)