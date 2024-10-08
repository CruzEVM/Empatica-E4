# Generated by Django 5.0.6 on 2024-07-04 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AnalisisTemperatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promedio', models.FloatField()),
                ('mediana', models.FloatField()),
                ('maximo', models.FloatField()),
                ('minimo', models.FloatField()),
                ('inicio_sesion', models.DateTimeField(blank=True, null=True)),
                ('tasa_muestreo', models.FloatField(blank=True, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e4data.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='AnalisisFrecuenciaCardiaca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promedio', models.FloatField()),
                ('mediana', models.FloatField()),
                ('maximo', models.FloatField()),
                ('minimo', models.FloatField()),
                ('inicio_sesion', models.DateTimeField(blank=True, null=True)),
                ('tasa_muestreo', models.FloatField(blank=True, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e4data.usuario')),
            ],
        ),
    ]
