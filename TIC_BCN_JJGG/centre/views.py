from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Context, loader
# Create your views here.

def index(request):
    professor = {}
    return render(request, 'index.html', {'nom':professor["nom"], 'surname':professor["surname"], 'age':professor["age"]})

def students(request):
    students = [{"nom"}]
    context = {'s':students}
    return render(request, 'users.html', context)

def teachers(request):
    teachers = [{
  {
            'id': 1,
            'nom': 'Xavi',
            'cognom1': 'Quesada',
            'cognom2': 'Puertas',
            'correu': 'xavi@iticbcn.cat',
            'curs': 'ASIX2A',
            'moduls': 'M08, MAH'
        },
  {
            'id': 2,
            'nom': 'Roger',
            'cognom1': 'Sobrino',
            'cognom2': 'Gil',
            'correu': 'roger@iticbcn.cat',
            'curs': 'DAM2B',
            'moduls': 'M07'
        },
        {
            'id': 3,
            'nom': 'Juanma',
            'cognom1': 'Sanchez',
            'cognom2': 'Bel',
            'correu': 'juanma@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06'
        }, 
        {
            'id': 4,
            'nom': 'Oriol',
            'cognom1': 'Roca',
            'cognom2': 'Fabra',
            'correu': 'oriol@iticbcn.cat',
            'curs': 'DAW2B',
            'moduls': 'M09'
        }
      
      }]
    context = {'t':teachers}
    return render(request, 'professors.html', context)

def users(request):
    a = True
    context = {'a' : a}
    return render(request, 'users.html',context)