from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Context, loader
# Create your views here.

def index(request):
    professor = {"nom":"Roger","surname":"Sobrino", "age": "37"}
    return render(request, 'index.html', {'nom':professor["nom"], 'surname':professor["surname"], 'age':professor["age"]})

def students(request):
    students = []
    context = {'s':students}
    return render(request, 'users.html', context)

def teachers(request):
    teachers = []
    context = {'t':teachers}
    return render(request, 'professors.html', context)

def users(request):
    a = True
    context = {'a' : a}
    return render(request, 'users.html',context)