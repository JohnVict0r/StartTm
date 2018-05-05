from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Categoria(models.Model):
    RATING = 'RAT'
    RANKING = 'RANK'

    MASCULINO = 'MASC'
    FEMININO = 'FEM'

    OLIM = 'OLIM'
    PARAOLIM = 'PARAOLIM'


    #DIVISAO_CATEGORIA = (
    #    ('A'),
    #    ('B'),
    #    ('C'),
    #
    #
    #    ('Absoluto A'),
    #    ('Absoluto B'),
    #
    #
    #    ('Mirim'),
    #    ('Juvenil'),
    #    ('Juventude'),
    #
    #
    #    ('Classe 01'),
    #    ('Classe 02'),
    #    ('Classe 03'),
    #)


    TIPO_CATEGORIA = (
        (RATING, 'Rating' ),
        (RANKING,'Ranking'),
    )

    SEXO_CATEGORIA = (
        (MASCULINO,'Masculino'),
        (FEMININO, 'Feminino'),
    )

    MODALIDADE_CATEGORIA = (
        (OLIM,  'Olimpico'),
        (PARAOLIM,  'Paraolimpico'),
    )


    divisao=models.CharField(
        max_length=10,
        #choices=DIVISAO_CATEGORIA,
        null=False,
    )
    sexo = models.CharField(
        max_length=10,
        choices=SEXO_CATEGORIA,
        default=MASCULINO,
        null=False,
    )
    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CATEGORIA,
        default=RATING,
        null=False,
    )
    modalidade = models.CharField(
        max_length=12,
        choices=MODALIDADE_CATEGORIA,
        default=OLIM,
        null=False,
    )

    pass




