from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse("Hola Index keloke")

def students(request):
    return HttpResponse("Hola student keloke")

def teachers(request):
    return HttpResponse("Hola profe keloke")