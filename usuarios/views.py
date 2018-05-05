from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.base import View
from perfis.models import Pessoa
from usuarios.forms import RegistrarUsuarioForm

# Create your views here.

class RegistrarUsuarioView(View):
    template_name = 'usuarios/registrar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
       
    	#preenche o from
        form = RegistrarUsuarioForm(request.POST)

        #verifica se eh valido
        if form.is_valid():

            dados_form = form.data

            #cria o usuario
            usuario = User.objects.create_user(dados_form['login'], dados_form['email'], dados_form['senha'])            

            #cria o perfil
            pessoa = Pessoa(

							nome = dados_form['nome'],
							sobrenome = dados_form['sobrenome'],
							
							cpf =  dados_form['cpf'],
							#dataNascimento = models.DateField(auto_now=False, auto_now_add=False)
							sexo = dados_form['sexo'],
                            usuario=usuario
                    )

            #grava no banco
            pessoa.save()

            #redireciona para index
            return redirect('index')

        #so chega aqui se nao for valido
        #vamos devolver o form para mostrar o formulario preenchido 
        return render(request, self.template_name, {'form' : form})





       #return render(request, self.template_name)
