# Generated by Django 2.2.12 on 2020-05-08 19:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recurso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='-', max_length=200, verbose_name='Nombre')),
                ('ancho_resolucion', models.IntegerField(default=1, verbose_name='Id')),
                ('alto_resolucion', models.IntegerField(default=1, verbose_name='Id')),
                ('sincronizado_al_servidor', models.BooleanField(verbose_name='Sincronizado al servidor')),
                ('tipo', models.CharField(choices=[('Archivos', 'Archivos'), ('Videos', 'Videos'), ('Streaming', 'Streaming')], default='Videos', max_length=50, verbose_name='Tipo')),
                ('reproduccion_automatica', models.BooleanField(verbose_name='Reproduccion automatica')),
                ('archivos', models.FileField(default='default.png', upload_to='', verbose_name='Archivos')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Ultima modificacion')),
            ],
            options={
                'verbose_name': 'Contenido',
                'verbose_name_plural': 'Contenido',
                'ordering': ['-nombre'],
            },
        ),
    ]