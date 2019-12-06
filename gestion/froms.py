from django import forms
from .models import Clientes

class ClientesForm(forms.ModelForm):   
    class Meta: #meta datos que va a manejar
        model = Clientes  
        fields = ['nombre_cliente' ,  'direccion' , 'email'  'Genero',]


