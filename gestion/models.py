from django.db import models
from django import forms
from django.utils.html import format_html
from django.urls import reverse
# Create your models here.

class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key= True)
    nombre_cliente = models.CharField('TU NOMBRE ' , max_length=120, blank= False , null= False)
    direccion = models.CharField('TU DIRECCION', max_length=120, blank= False , null= False )    
    email = models.EmailField('TU CORREO ELECTRONICO:' ,max_length=200, blank= False , null= False )
    
    LOAN_STATUS = (  #combobox 
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('-', 'No especificado'),
    )
    
    genero = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='-',
        help_text='genero',
    )


    class Meta:  
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre_cliente']

    def get_absolute_url(self):
        return reverse('cliente_detail', args=[str(self.id_cliente)])#es aquiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii

    def __str__(self):
        return self.nombre_cliente 
    
    


class generoJuego(models.Model):
    id_generoJuego= models.AutoField(primary_key= True , max_length=10)
    nombre_genero = models.CharField('Genero del juego: ',max_length=120,blank= False , null= False )

       
    def __str__(self):
        return self.nombre_genero 


class desarrolladora(models.Model):
    id_desarrolladora = models.AutoField(primary_key= True , max_length=10)
    nombre_desarrolladora = models.CharField('Nombre de la desarrolladora: ',max_length=120,blank= False , null= False)
    fecha_creacion = models.DateField(blank= False , null= False)

    class Meta:
        verbose_name = 'Desarrolladora'
        verbose_name_plural = 'Desarrolladoras'
        ordering = ['nombre_desarrolladora']

    def __str__(self):
        return self.nombre_desarrolladora 

class juegos(models.Model):
    id_juego= models.AutoField(primary_key= True)
    nombreJuego = models.CharField('Nombre del juego: ' , max_length=120)
    precio = models.IntegerField('Precio del juego:',blank= False , null= False)
    fecha_publicacion = models.DateField('Fecha de publicacion del juego :',blank= False , null= False)

    #Relaciones
    desarrolladora_id = models.OneToOneField(desarrolladora , on_delete = models.CASCADE)  #uno a uno
    #genero_id = models.ForeignKey(generoJuego , on_delete = models.CASCADE) #uno a muchos
    genero_id = models.ManyToManyField(generoJuego) #muchos a muchos


    class Meta:
        verbose_name = 'Juego'
        verbose_name_plural = 'Juegos'
        ordering = ['nombreJuego']

    def __str__(self):
        return self.nombreJuego #Al listar en el menu de ad, nombre/sinonimo del nombre que se mostrara al listarlo en el menu de ad
 

        

 