from __future__ import unicode_literals

from django.db import models

class Atleta(models.Model):


    def __str__(self):
        return self.name