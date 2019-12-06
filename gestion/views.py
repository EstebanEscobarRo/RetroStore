from django.views.generic.edit import CreateView , UpdateView , DeleteView#
from django.urls import reverse_lazy#
from .models import Clientes#
from django.views import generic
from django.views.generic import ListView
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms


# Create your views here.
def home (request):

    return render(request,"home.html" )


def encuentranos (request):

    return render(request,"encuentranos.html" )    

def juegos (request):

    return render(request,"juegos.html" )

class ClienteCreate(CreateView):
    model = Clientes
    fields = '__all__'
    initial = {'email':'@'}


class ClienteUpdate(UpdateView):
    model = Clientes
    fields = {'nombre_cliente', 'direccion', 'email' , 'genero'} #en models

class ClienteDelete(DeleteView):
    model = Clientes
    success_url = reverse_lazy('clientes')


class ClienteDetailView(generic.DetailView):
    model = Clientes

class ClienteList(ListView):
    model = Clientes 

#Posible error /

"""def add_cliente(request):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = ClienteForm(request.POST) # Bound form
        if form.is_valid():
            new_persona = form.save() # Guardar los datos en la base de datos

            return HttpResponseRedirect(reverse('padd:plist'))#
    else:
        form = ClienteForm() # Unbound form

    return render(request, 'cliente_form.html', {'form': form})"""