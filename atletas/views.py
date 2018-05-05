from django.shortcuts import render

from .models import Atleta



def atleta_list(request):
    atletas = Atleta.objects.all()
    context = {
       'atletas_list': atletas
    }
    return render(request, 'atletas/listar.html', context)

def cadastrar_atleta(request):
    return render(request, 'atletas/cadastrar.html')