import datetime
from datetime import date

from django.db import models
from django.db.models.base import Model

from usuarios.models import Usuario


class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome


class Livros(models.Model):
    nome = models.CharField(max_length = 100, blank = True)
    autor = models.CharField(max_length = 30, blank = True)
    co_autor = models.CharField(max_length = 30, blank = True)
    data_cadastro = models.DateField(default = date.today)
    emprestado = models.BooleanField(default = False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    localizacao = models.CharField(max_length = 100, verbose_name='Localização')
    exemplares_disponiveis = models.CharField(max_length = 100)
    compositor = models.CharField(max_length = 100, blank = True, verbose_name='Compositor')
    arranjador = models.CharField(max_length = 100, blank = True, verbose_name='Arranjador')
    obra = models.CharField(max_length = 100, verbose_name='Obra')
    classificacao = models.CharField(max_length = 100, verbose_name='Classificação')
    conteudo = models.CharField(max_length = 100, verbose_name='Conteúdo')
    edicao = models.CharField(max_length = 100, verbose_name='Edição')
    observacao = models.CharField(max_length = 100, blank = True, verbose_name='Observação')
    formato = models.CharField(max_length = 100, verbose_name='Formato')


    class Meta:
        verbose_name = 'Partitura'

    def __str__(self):
        return self.nome

class Emprestimos(models.Model):
    choices = (
        ('P', 'Péssimo'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('O', 'Ótimo')
    )
    nome_emprestado = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, blank = True, null = True)
    nome_emprestado_anonimo = models.CharField(max_length = 30, blank = True, null = True)
    data_emprestimo = models.DateTimeField(default=datetime.datetime.now())
    data_devolucao = models.DateTimeField(blank = True, null = True)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)
    avaliacao = models.CharField(max_length=1, choices=choices, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nome_emprestado} | {self.livro}"



