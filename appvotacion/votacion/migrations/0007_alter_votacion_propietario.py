# Generated by Django 4.0.4 on 2022-12-27 00:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('votacion', '0006_alter_candidato_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votacion',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Propietario'),
        ),
    ]
