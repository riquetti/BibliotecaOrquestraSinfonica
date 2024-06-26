# Generated by Django 5.0.4 on 2024-04-05 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0015_alter_emprestimos_livro'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='livros',
            options={'verbose_name': 'Partitura'},
        ),
        migrations.AddField(
            model_name='livros',
            name='exemplares_disponiveis',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livros',
            name='localizacao',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
