# Generated by Django 4.2.13 on 2024-06-18 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0003_alter_usuario_nome'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usuario',
            unique_together={('nome', 'idade')},
        ),
    ]
