from django.http import HttpResponse
from django.shortcuts import render
from .models import Mis_datos, Cursos, Habilidades_blandas


# Create your views here.

def curso(request):
    curso = Cursos(nombre= "Python para no programadores",fecha=2022,institucion= " Educacion IT")
    curso.save()
    texto=f" Asi creo los cursos que he hecho {curso.nombre} fecha {curso.fecha} e institucion{curso.institucion} "
    return render (request, "AppPortfolio/cursos.html")
    


def inicio(request):
    return render (request, "AppPortfolio/inicio.html")

def mis_datos(request):
    return render (request, "AppPortfolio/misdatos.html")

def habilidades_blandas(request):
    return render (request, "AppPortfolio/habilidades.html")  