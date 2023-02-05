from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login, logout
from articulos.models import Entrada,Comentario
from articulos.forms import ComentarioForm
from django.db import IntegrityError

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def home(request) :
    articulos = Entrada.objects.all()
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            comentario = form.cleaned_data['comentario']
            obj = Comentario(nombre=nombre,comentario=comentario)
            obj.save()
            mensaje = "thanks"
            form = ComentarioForm()
        return render(request, 'bienvenidos.html', {'articulos': articulos, 'mensaje': mensaje,'form':form})
    form = ComentarioForm()
    return render(request, 'bienvenidos.html', {'articulos':   articulos,'form':form })

def crearcuenta(request):
    if request.method == 'GET':
         return render(request, 'crearcuenta.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2'] :
            try:
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('tasks')
            except IntegrityError:    
                return render(request, 'crearcuenta.html', {'form': UserCreationForm, "error": 'Usuario ya existe'})
        return render(request, 'crearcuenta.html', {'form': UserCreationForm, "error": 'Passwords no coinciden'})


def tasks(request):
    return render (request, 'tasks.html')

def cerrarsesion(request): 
    logout(request)
    return redirect('inicio')

def iniciarsesion(request):
    return render (request, 'iniciarsesion.html',  {'form': AuthenticationForm})

def comentario(request):
    articulos = Entrada.objects.all()
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            comentario = form.cleaned_data['comentario']
            obj = Comentario(nombre=nombre,comentario=comentario)
            obj.save()
            mensaje = "thanks"
            form = ComentarioForm()
        return render(request, 'bienvenidos.html', {'articulos': articulos, 'mensaje': mensaje,'form':form})
    form = ComentarioForm()
    return render(request, 'bienvenidos.html', {'articulos':   articulos,'form':form })