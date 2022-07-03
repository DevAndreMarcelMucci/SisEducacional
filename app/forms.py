"""
Definition of forms.
"""
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

    #class InsereProfessorForm(forms.ModelForm):
    #    nomeProf = forms.CharField(
    #        max_length = 255,
    #        null=False,
    #        blank=False
    #        )
    #    cpfProf = forms.CharField(
    #     max_length = 14,
    #        null = False,
    #        blank = False
    #        )

    ##   Calsse Turma
    #class InsereTurmaForm(forms.ModelForm):
    #    nomeTurma = forms.CharField(
    #        max_length = 255,
    #        null=False,
    #        blank=False
    #        )

    ##   Calsse Aluno
    #class Aluno(models.Model):
    #    nomeAluno = forms.CharField(
    #        max_length = 255,
    #        null=False,
    #        blank=False
    #        )
    #    cpfAluno = forms.CharField(
    #        max_length = 14,
    #        null = False,
    #        blank = False
    #        )


        # Se quiser inserir mais campos no formulario
        # Exemplo
        #   chefe = forms.BooleanField(
        #     label='Chefe?',
        #     required=True,
        #     )
        #     biografia = forms.CharField(
        #     label='Biografia',
        #     required=False,
        #     widget=forms.TextArea
        #     )

        #class Meta:
        #    # Model base
        #    model = Professor
            
        #    # Campos que estarão no form
        #    fields = [
        #        'nomeProf',
        #        'cpfProf',
        #        ]
            
        #    # Campos que ficaram fora do form
        #    exclude = [
        #        # aqui colocaria os campos que ficaram de fora
        #        ]
            
        #class InsereAluno(forms.Form):
        #    class Meta:
        #        # Model base
        #        model = Aluno
            
        #    # Campos que estarão no form
        #    fields = [
        #        'nomeAluno',
        #        'cpfAluno',
        #        ]

        #class InsereTurma(forms.Form):
        #    class Meta:
        #        # Model base
        #        model = Turma
            
        #    # Campos que estarão no form
        #    fields = [
        #        'nomeTurma',
                
        #        ]

