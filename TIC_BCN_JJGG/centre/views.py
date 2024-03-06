from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def students(request):
    return HttpResponse("Hola student keloke")

def teachers(request):
    return HttpResponse("Hola profe keloke")