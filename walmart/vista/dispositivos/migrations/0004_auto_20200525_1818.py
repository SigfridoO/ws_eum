# Generated by Django 2.2.12 on 2020-05-25 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivos', '0003_auto_20200525_1817'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dispositivo',
            options={'ordering': ['-prioridad'], 'verbose_name': 'Dispositivo', 'verbose_name_plural': 'Dispositivo'},
        ),
        migrations.RenameField(
            model_name='dispositivo',
            old_name='numero',
            new_name='prioridad',
        ),
    ]
