from django.shortcuts import render,redirect
from .models import Cliente
# Create your views here.

def inicio_vista(request):
    losclientes=Cliente.objects.all()

    return render(request,"gestionarCliente.html",{"losclientes":losclientes})


def registrarCliente(request):
    id_cliente =request.POST["txtid_cliente"]
    nombre =request.POST["txtnombre"]
    apellido  =request.POST["txtapellido"]
    email  =request.POST["txtemail"] 
    telefono  =request.POST["txttelefono"]
    direccion  =request.POST["txtdireccion"]
    guardar=Cliente.objects.create(id_cliente=id_cliente,nombre=nombre,apellido=apellido,
    email=email,telefono=telefono,direccion=direccion)
    return redirect("cliente")

def seleccionarCliente(request,id_cliente):
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    return render(request,"editarCliente.html",{"losclientes":cliente})

def editarCliente(request):
    id_cliente =request.POST["txtid_cliente"]
    nombre =request.POST["txtnombre"]
    apellido  =request.POST["txtapellido"]
    email  =request.POST["txtemail"] 
    telefono  =request.POST["txttelefono"]
    direccion  =request.POST["txtdireccion"]
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre=nombre
    cliente.apellido=apellido
    cliente.email=email
    cliente.telefono=telefono
    cliente.direccion=direccion
    cliente.save()
    return redirect("cliente")

def borrarCliente(request,id_cliente):
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect("cliente")