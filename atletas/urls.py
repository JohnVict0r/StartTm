from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^atletas/listar$', views.atleta_list, name='list'),
    url(r'^atletas/$', views.cadastrar_atleta, name='cadastrar_atleta')
]