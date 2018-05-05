from django.shortcuts import render
from django.shortcuts import redirect

from perfis.models import Perfil
from eventos.models import EventoCategoria, Evento, InscricaoSolicitacao
from categorias.models import Categoria


def index(request):
    return render(request, 'eventos/lista-eventos.html', {'eventos': Evento.objects.all(),'perfil_logado' : get_perfil_logado(request)})


#def atletas(request):
 #   return render(request, 'atletas/cadastrar-Alga.html')


def exibir_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    evento_categoria= EventoCategoria.objects.filter(evento_id = evento_id)




    p = get_perfil_logado(request)

    i = InscricaoSolicitacao.objects.filter(solicitante=p)

    return render(request, 'eventos/eventos.html', {"evento": evento , "categoria": evento_categoria ,"inscrito": i, 'perfil_logado' : get_perfil_logado(request)})

def exibir_evento_categoria(request, evento_id, evento_categoria_id):

    return render(request, 'eventos/lista-eventos.html', {'eventos': Evento.objects.all()})
    #evento_categoria = Evento.objects.get(id=evento_id)


def inscrever(request, evento_id, evento_categoria_id):
    evento_categoria_a_inscrever = EventoCategoria.objects.get(id=evento_categoria_id)
    perfil_logado = get_perfil_logado(request)
    evento_categoria_a_inscrever.solicitar_incricao(perfil_logado)

    return redirect('index')


def get_perfil_logado(request):
    return Perfil.objects.get(id=1)