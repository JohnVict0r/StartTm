from __future__ import unicode_literals
from django.db import models

from atletas.models import Atleta
from perfis.models import Perfil
from categorias.models import  Categoria

class Evento(models.Model):

	nome = models.CharField(max_length=255, null=False)
	local = models.CharField(max_length=255, null=False)
	ano = models.CharField(max_length=4, null=False)

	def solicitar_incricao(self, perfil_logado):
		InscricaoSolicitacao(solicitante=perfil_logado, solicitacao=self).save()


class EventoCategoria(models.Model):

    evento = models.ForeignKey(Evento, related_name='evento_evento_categoria', on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, related_name='evento_categoria', on_delete=models.CASCADE)





class InscricaoSolicitacao(models.Model):

	solicitante = models.ForeignKey(Perfil, related_name='solicitante_incricao', on_delete=models.CASCADE)
	solicitacao = models.ForeignKey(EventoCategoria, related_name='solicitacao_evento', on_delete=models.CASCADE)
	#atleta = models.ForeignKey(atleta, related_name='atleta_inscricao')

class Inscricao(models.Model):
    pass