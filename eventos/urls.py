from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^eventos/(?P<evento_id>\d+)$', views.exibir_evento, name='exibir_evento'),
    url(r'^eventos/(?P<evento_id>\d+)/(?P<evento_categoria_id>\d+)$', views.exibir_evento_categoria, name='exibir_evento_categoria'),
	url(r'^eventos/(?P<evento_id>\d+)/(?P<evento_categoria_id>\d+)/solicitar_inscricao$', views.inscrever, name='solicitar_inscricao'),

]