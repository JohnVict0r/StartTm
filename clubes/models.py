from __future__ import unicode_literals

from django.db import models

from atletas.models import Atleta
from tecnicos.models import Tecnico
# Create your models here.

class Clube(models.Model):
    nome = models.CharField(max_length=255, null=False)
    sigla = models.CharField(max_length=255, null=False)
    #cidade=
    #estado=
class AtletaClube(models.Model):

    clube = models.ForeignKey(Clube, on_delete=models.CASCADE)
    atletas = models.ForeignKey(Atleta, on_delete=models.CASCADE)


#class TecnicoClube(models.Model):
    #clube = models.ForeingKey(Clube, on_delete=models.CASCADE)
    #tecnicos = models.ForeingKey(Tecnico,reletad_name="tecnico_clube",on_delete=models.CASCADE)

