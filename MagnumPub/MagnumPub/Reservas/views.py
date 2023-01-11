from http.client import HTTPResponse
from django.shortcuts import render
from django.template import loader
from .forms import UsuarioForm
from .models import Usuario
import datetime


def inicio (request):
    if request.method == "POST":
        form=UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error",form.errors)
    form=UsuarioForm()    
    return render (request,"inicio.html",{'form':form})

def vista (request):   
    lista = Usuario.objects.all()    
    return render(request, "vista.html",{"reserva": lista} )

def eliminar_reserva(request,id):
    
    if request.method == "POST":
        
        eliminar= Usuario.objects.get(id=id)
        eliminar.delete()        
       
        
        return render(request, "vista.html", {'eliminar': eliminar})    