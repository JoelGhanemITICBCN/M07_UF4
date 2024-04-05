from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.template import Context, loader
from .models import Usuari
from .forms import UsuariForm
from centre.models import Usuari

# Create your views here.

def index(request):
    professor = {}
    return render(request, 'index.html')

# Mas de uno
def students(request):
    estudiants = Usuari.objects.filter(rol='alumne')
    return render(request, 'users.html', {'estudiants' : estudiants})

def teachers(request):
    profes = Usuari.objects.filter(rol='professor')
    return render(request, 'professors.html', {'profes' : profes})

# Solo uno
def student(request,pk) :
    estudiant = Usuari.objects.get(id=pk)
    return render(request, 'user.html', {'s': estudiant})


def teacher(request, pk):
    profe = Usuari.objects.get(id=pk)
    return render(request, 'professor.html', {'t': profe})

def user_form(request):
    form = UsuariForm()
    
    if request.method == 'POST': 
        form = UsuariForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    return render(request,'form.html',context)

def update_user(request, pk):
    usuari = Usuari.objects.get(id=pk)  
    form = UsuariForm(request.POST or None, instance=usuari)  

    if form.is_valid():
        form.save()
        return redirect('index')  

    return render(request, 'form.html', {'form': form}) 

def delete_user(request, pk):
    person = Usuari.objects.get(id=pk)
    if request.method == 'POST':
        person.delete()
        return redirect('index')
        
    context = {'object': person}
    return render(request, 'delete.html', context)