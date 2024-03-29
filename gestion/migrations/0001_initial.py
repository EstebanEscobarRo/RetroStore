# Generated by Django 2.2.7 on 2019-11-18 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=120)),
                ('direccion', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('sexo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='desarrolladora',
            fields=[
                ('id_desarrolladora', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_desarrolladora', models.CharField(max_length=150)),
                ('fecha_creacion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='generoJuego',
            fields=[
                ('id_generoJuego', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_genero', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='juegos',
            fields=[
                ('id_juego', models.AutoField(primary_key=True, serialize=False)),
                ('nombreJuego', models.CharField(max_length=120, verbose_name='Nombre del juego: ')),
                ('genero', models.CharField(max_length=120, verbose_name='Genero del juego: ')),
                ('precio', models.IntegerField(verbose_name='Precio del juego:')),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha de publicacion del juego :')),
                ('desarrolladora_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestion.desarrolladora')),
                ('genero_id', models.ManyToManyField(to='gestion.generoJuego')),
            ],
        ),
    ]
