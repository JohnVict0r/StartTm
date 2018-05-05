from django import forms
from django.contrib.auth.models import User
from django.forms import ComboField

class RegistrarUsuarioForm(forms.Form):

	M= "Masculino"
	F = "Feminino"

	SEXO=((M,"Masculino"),
		  (F,"Feminino"),
		  )

	email = forms.EmailField(required=True)
	nome = forms.CharField(required=True)
	sobrenome=forms.CharField(required=True)
	login = forms.CharField(required=True)
	senha = forms.CharField(required=True)

	#telefone = forms.CharField(required=True)

	#sexo = forms.ComboField(required=True)
	#sexo = forms.CharField(
	#	max_length=30,
	#	#choices=SEXO,
	#	# default=AT,
	#	required=True,
	#)

	CHOICES = ((M,"Masculino"), (F,"Feminino"),)
	sexo = forms.ChoiceField(choices=CHOICES)


	def is_valid(self):
		valid = True

		if not super(RegistrarUsuarioForm, self).is_valid():
			self.adiciona_erro('Por favor, verifique os dados informados')
			valid = False

		user_exists = User.objects.filter(username=self.data['login']).exists()

		if user_exists:
			self.adiciona_erro('Usuario ja existente')
			valid = False

		return valid
		
	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)