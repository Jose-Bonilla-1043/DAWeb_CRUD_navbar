from django.shortcuts import render,redirect
from .models import Producto
# Create your views here.

def inicio_vista(request):
    elproducto=Producto.objects.all()
    return render(request,"gestionarProducto.html",{"elproducto":elproducto})


def registrarProducto(request):
    id_producto =request.POST["txtid_producto"]
    nombre =request.POST["txtnombre"]
    descripcion  =request.POST["txtdescripcion"]
    tamano  =request.POST["txttamano"] 
    color  =request.POST["txtcolor"]
    precio  =request.POST["numprecio"]
    marca  =request.POST["txtmarca"]
    guardar=Producto.objects.create(id_producto=id_producto,nombre=nombre,descripcion=descripcion,
    tamano=tamano,color=color,precio=precio,marca=marca)
    return redirect("producto")

def seleccionarProducto(request,id_producto):
    producto=Producto.objects.get(id_producto=id_producto)
    return render(request,"editarProducto.html",{"elproducto":producto})

def editarProducto(request):
    id_producto =request.POST["txtid_producto"]
    nombre =request.POST["txtnombre"]
    descripcion  =request.POST["txtdescripcion"]
    tamano  =request.POST["txttamano"] 
    color  =request.POST["txtcolor"]
    precio  =request.POST["numprecio"]
    marca  =request.POST["txtmarca"]
    producto=Producto.objects.get(id_producto=id_producto)
    producto.nombre=nombre
    producto.descripcion=descripcion
    producto.tamano=tamano
    producto.color=color
    producto.precio=precio
    producto.marca=marca
    producto.save()
    return redirect("producto")

def borrarProducto(request,id_producto):
    producto=Producto.objects.get(id_producto=id_producto)
    producto.delete()
    return redirect("producto")