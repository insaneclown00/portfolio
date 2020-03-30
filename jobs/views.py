from django.shortcuts import render
from .models import Job, Contact
from django.contrib import messages

# Create your views here.
def home(request):
	jobs = Job.objects
	return render(request, 'jobs/index-dark.html',{'jobs':jobs})


def contact(request):
	if request.method=='POST':
		print('We are using POST')
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']
		print(name, email, message)
		contact = Contact(name=name, email=email, message=message)
		contact.save()
		
		return render(request, 'jobs/index-dark.html',{'contact':contact})
