# Generated by Django 5.0.3 on 2024-03-26 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0003_alter_livros_co_autor_alter_livros_data_devolucao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='data_cadastro',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
