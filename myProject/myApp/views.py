from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Docker World! You're at the homepage of my Django App.")
    
