from django.shortcuts import render,redirect
from .models import Proveedor
# Create your views here.

def inicio_vista(request):
    elproveedor=Proveedor.objects.all()

    return render(request,"gestionarProveedor.html",{"elproveedor":elproveedor})


def registrarProveedor(request):
    id_proveedor =request.POST["txtid_proveedor"]
    nombre =request.POST["txtnombre"]
    contacto  =request.POST["txtcontacto"]
    telefono  =request.POST["txttelefono"] 
    direccion  =request.POST["txtdireccion"]
    ciudad  =request.POST["txtciudad"]
    guardar=Proveedor.objects.create(id_proveedor=id_proveedor,nombre=nombre,contacto=contacto,
    telefono=telefono,direccion=direccion,ciudad=ciudad)
    return redirect("proveedor")

def seleccionarProveedor(request,id_proveedor):
    proveedor=Proveedor.objects.get(id_proveedor=id_proveedor)
    return render(request,"editarProveedor.html",{"elproveedor":proveedor})

def editarProveedor(request):
    id_proveedor =request.POST["txtid_proveedor"]
    nombre =request.POST["txtnombre"]
    contacto  =request.POST["txtcontacto"]
    telefono  =request.POST["txttelefono"] 
    telefono   =request.POST["txtdireccion"]
    ciudad  =request.POST["txtciudad"]
    proveedor=Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.nombre=nombre
    proveedor.contacto=contacto
    proveedor.telefono=telefono
    proveedor.ciudad=ciudad
    proveedor.save()
    return redirect("proveedor")

def borrarProveedor(request,id_proveedor):
    proveedor=Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.delete()
    return redirect("proveedor")