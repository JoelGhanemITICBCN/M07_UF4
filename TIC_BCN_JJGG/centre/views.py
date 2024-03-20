from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Context, loader
# Create your views here.

def index(request):
    professor = {}
    return render(request, 'index.html')

def students(request):
    students = [
        {
            'id': 1,
            'nom': 'Alexander',
            'cognom1': 'Andreev',
            'cognom2': 'Apukhtina',
            'correu': 'alexander@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 2,
            'nom': 'Jesus',
            'cognom1': 'Pujada',
            'cognom2': 'Montoya',
            'correu': 'oriana@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 3,
            'nom': 'Joel',
            'cognom1': 'Ghanem',
            'cognom2': 'Gomez',
            'correu': 'joel@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 4,
            'nom': 'Dinar',
            'cognom1': 'Khazimullin',
            'cognom2': '',
            'correu': 'dinar@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 5,
            'nom': 'Anxo',
            'cognom1': 'Aragundi',
            'cognom2': 'Mesias',
            'correu': 'anxo@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 6,
            'nom': 'Carlos ',
            'cognom1': 'Zambrano',
            'cognom2': 'Aray',
            'correu': 'andres@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 7,
            'nom': 'Angel',
            'cognom1': 'Ivanov',
            'cognom2': 'Spasov',
            'correu': 'angel@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
     
    ]
    context = {'s':students}
    return render(request, 'users.html', context)

def teachers(request):
    teachers = [
  {
            'id': 1,
            'nom': 'Xavi',
            'cognom1': 'Quesada',
            'cognom2': 'Puertas',
            'correu': 'xavi@iticbcn.cat',
            'curs': 'ASIX2A',
            'tutor': False,
            'moduls': 'M08, MAH'
        },
  {
            'id': 2,
            'nom': 'Roger',
            'cognom1': 'Sobrino',
            'cognom2': 'Gil',
            'correu': 'roger@iticbcn.cat',
            'curs': 'DAM2B',
            'tutor': False,
            'moduls': 'M07'
        },
        {
            'id': 3,
            'nom': 'Juanma',
            'cognom1': 'Sanchez',
            'cognom2': 'Bel',
            'correu': 'juanma@iticbcn.cat',
            'curs': 'DAW2A',
            'tutor': True,
            'moduls': 'M06'
        },  
        {
            'id': 4,
            'nom': 'Oriol',
            'cognom1': 'Roca',
            'cognom2': 'Fabra',
            'correu': 'oriol@iticbcn.cat',
            'curs': 'DAW2B',
            'tutor': False,
            'moduls': 'M09'
      }
        ]

    context = {'t':teachers}
    return render(request, 'professors.html', context)

def student(request,pk) :
    students = [
        {
            'id': 1,
            'nom': 'Alexander',
            'cognom1': 'Andreev',
            'cognom2': 'Apukhtina',
            'correu': 'alexander@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 2,
            'nom': 'Jesus',
            'cognom1': 'Pujada',
            'cognom2': 'Montoya',
            'correu': 'oriana@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 3,
            'nom': 'Joel',
            'cognom1': 'Ghanem',
            'cognom2': 'Gomez',
            'correu': 'joel@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 4,
            'nom': 'Dinar',
            'cognom1': 'Khazimullin',
            'cognom2': '',
            'correu': 'dinar@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 5,
            'nom': 'Anxo',
            'cognom1': 'Aragundi',
            'cognom2': 'Mesias',
            'correu': 'anxo@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 6,
            'nom': 'Carlos ',
            'cognom1': 'Zambrano',
            'cognom2': 'Aray',
            'correu': 'andres@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        },
        {
            'id': 7,
            'nom': 'Angel',
            'cognom1': 'Ivanov',
            'cognom2': 'Spasov',
            'correu': 'angel@iticbcn.cat',
            'curs': 'DAW2A',
            'moduls': 'M06, M07, M08, M09, MAH'
        }
     
    ]
    estudiant = None
    for i in students:
        if i['id'] == pk:
            estudiant = i
    return render(request, 'user.html', {'s': estudiant})


def teacher(request, pk):
    teachers = [
  {
            'id': 1,
            'nom': 'Xavi',
            'cognom1': 'Quesada',
            'cognom2': 'Puertas',
            'correu': 'xavi@iticbcn.cat',
            'curs': 'ASIX2A',
            'tutor': False,
            'moduls': 'M08, MAH'
        },
  {
            'id': 2,
            'nom': 'Roger',
            'cognom1': 'Sobrino',
            'cognom2': 'Gil',
            'correu': 'roger@iticbcn.cat',
            'curs': 'DAM2B',
            'tutor': False,
            'moduls': 'M07'
        },
        {
            'id': 3,
            'nom': 'Juanma',
            'cognom1': 'Sanchez',
            'cognom2': 'Bel',
            'correu': 'juanma@iticbcn.cat',
            'curs': 'DAW2A',
            'tutor': True,
            'moduls': 'M06'
        },  
        {
            'id': 4,
            'nom': 'Oriol',
            'cognom1': 'Roca',
            'cognom2': 'Fabra',
            'correu': 'oriol@iticbcn.cat',
            'curs': 'DAW2B',
            'tutor': False,
            'moduls': 'M09'
      }
        ]

    profe = None
    for i in teachers:
        if i['id'] == pk:
            profe = i
    return render(request, 'professor.html', {'t': profe})
