# Generated by Django 4.0.4 on 2022-12-08 00:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='candidato',
            fields=[
                ('ide', models.AutoField(primary_key=True, serialize=False)),
                ('tarjeton', models.CharField(max_length=4, verbose_name='Número de Tarjeton')),
                ('imagen', models.ImageField(upload_to='candidatos', verbose_name='Imagen')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='votacion',
            fields=[
                ('ide', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre Votación')),
                ('descripcion', models.CharField(max_length=250, verbose_name='Descripción Votación')),
                ('fecha_inicio', models.DateTimeField(verbose_name='Fecha de Inicio')),
                ('fecha_fin', models.DateTimeField(verbose_name='Fecha de FInalización')),
            ],
        ),
        migrations.CreateModel(
            name='votante',
            fields=[
                ('ide', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='votos',
            fields=[
                ('ide', models.AutoField(primary_key=True, serialize=False)),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votacion.candidato', verbose_name='Votación')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='votacion.votante', verbose_name='Votante')),
                ('votacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votacion.votacion', verbose_name='Votación')),
            ],
        ),
        migrations.AddField(
            model_name='candidato',
            name='votante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votacion.votante', verbose_name='Candidato'),
        ),
    ]
