# Generated by Django 5.0.3 on 2024-04-01 16:12

import livro.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0006_alter_livros_data_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='data_cadastro',
            field=models.DateTimeField(blank=True, default=livro.models.default_data_cadastro),
        ),
    ]