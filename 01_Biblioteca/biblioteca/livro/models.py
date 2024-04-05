from django.db import models
from django.utils import timezone

def default_data_cadastro():
    return timezone.now()

class Livros(models.Model):
    nome = models.CharField(max_length=200)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=100, blank=True, null = True)
    data_cadastro = models.DateTimeField(default=default_data_cadastro, blank=True)
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=30, blank=True)
    data_emprestimo = models.DateTimeField(blank=True)
    data_devolucao = models.DateTimeField(blank=True)
    tempo_emprestimo = models.TimeField(blank=True)

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.nome
