# Generated by Django 4.0.4 on 2022-12-27 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacion', '0007_alter_votacion_propietario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votante',
            name='votacion',
            field=models.JSONField(blank=True, null=True, verbose_name='Votaciones'),
        ),
    ]
