from django.http import HttpResponse
from django.shortcuts import render

def about(request):
	return HttpResponse('This is about page23345')

def home (request):
	return render(request, 'home.html')