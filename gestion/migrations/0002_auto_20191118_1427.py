# Generated by Django 2.2.7 on 2019-11-18 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juegos',
            name='genero',
        ),
        migrations.AlterField(
            model_name='desarrolladora',
            name='fecha_creacion',
            field=models.DateField(),
        ),
    ]
