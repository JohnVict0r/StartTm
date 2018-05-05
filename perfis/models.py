from django.db import models

from django.contrib.auth.models import User

class Perfil(models.Model):

	AT = 'Atleta'
	TE = 'Tecnico'
	PC = 'Presidente do Clube'
	PF = 'Presidente da Federação'
	AR = 'Arbitro'
	GE = 'Gestor de eventos'

	PERFIL = (
		(AT, 'Atleta'),
		(TE, 'Tecnico'),
		(PC, 'Presidente do Clube'),
		(PF, 'Presidente da Federação'),
		(AR, 'Arbitro'),
		#(AGE, 'Arbitro Geral do Evento'),
		(GE, 'Gestor de Eventos'),


	)

	perfil = models.CharField(
		max_length=30,
		choices=PERFIL,
		#default=AT,
		null=False,
	)




	#pessoa= models.ForeignKey(
	#	Pessoa,
	#	related_name='perfis',
	#	on_delete=models.CASCADE
	#)





class Pessoa(models.Model):
	nome = models.CharField(max_length=255, null=False)
	sobrenome = models.CharField(max_length=255, null=False)
	telefone = models.CharField(max_length=17)
	celular =  models.CharField(max_length=17)
	cpf =  models.CharField(max_length=14, null=False)
	rg =  models.CharField(max_length=17, null=False)
	#dataNascimento = models.DateField(auto_now=False, auto_now_add=False)
	sexo = models.CharField(max_length=10, null=True)

	usuario = models.OneToOneField(User, related_name="pessoa",on_delete=models.CASCADE)





	#def convidar(self, perfil_convidado):
	#	Convite(solicitante=self, convidado=perfil_convidado).save()

#class Convite(models.Model):
#
#	solicitante = models.ForeignKey(Perfil, related_name='convites_feitos')
#	convidado = models.ForeignKey(Perfil, related_name='convites_recebidos')