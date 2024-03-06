from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hola Index keloke")

def students(request):
    return HttpResponse("Hola student keloke")

def teachers(request):
    return HttpResponse("Hola profe keloke")