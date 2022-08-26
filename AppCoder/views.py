from django.shortcuts import render
from AppCoder.models import Curso, Entregable

def curso(request):

    curso1 = Curso(nombre='Python', camada=31095)
    curso1.save()
    contexto = {
        'curso': curso1
    }

    return render(request, 'AppCoder/curso.html', contexto)

def entregable(request):

    entregable1 = Entregable(nombre='Pepito', fecha_de_entrega='29/05/1956', entregado=True)
    #entregable1.save()
    contexto = {
        'entregable': entregable1
    }
    return render(request,'AppCoder/entregable.html', contexto)

def inicio(request):
    contexto = {
        'valor1': 'Este es un valor'
    }
    return render(request, 'index.html', contexto)