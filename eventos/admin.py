from django.contrib import admin
from .models import Evento, EventoCategoria, InscricaoSolicitacao
# Register your models here.

admin.site.register(Evento)
admin.site.register(EventoCategoria)
admin.site.register(InscricaoSolicitacao)