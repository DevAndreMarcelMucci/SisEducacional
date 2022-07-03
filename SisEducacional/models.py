"""
Definition of models.
"""

from django.db import models

#   Calsse Professor
class Professor(models.Model):

    nomeProf = models.CharField(
        max_length = 255,
        null=False,
        blank=False
        )
    cpfProf = models.CharField(
        max_length = 14,
        null = False,
        blank = False
        )

#   Calsse Turma
class Turma(models.Model):
    nomeTurma = models.CharField(
        max_length = 255,
        null=False,
        blank=False
        )

#   Calsse Aluno
class Aluno(models.Model):
    nomeAluno = models.CharField(
        max_length = 255,
        null=False,
        blank=False
        )
    cpfAluno = models.CharField(
        max_length = 14,
        null = False,
        blank = False
        )

objetos = models.Manager()