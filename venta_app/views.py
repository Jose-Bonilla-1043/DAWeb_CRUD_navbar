from django.shortcuts import render,redirect
from .models import Venta
# Create your views here.

def inicio_vista(request):
    lasventas = Venta.objects.all()
    return render(request, "gestionarVenta.html", {"lasventas": lasventas})



def registrarVenta(request):
    id_venta =request.POST["txtid_venta"]
    fecha =request.POST["datefecha"]
    estado  =request.POST["txtestado"]
    cantidad  =request.POST["numcantidad"] 
    precio_total  =request.POST["numprecio"]
    id_producto  =request.POST["txtid_producto"]
    id_empleado  =request.POST["txtid_empleado"]
    id_cliente  =request.POST["txtid_cliente"]
    guardar=Venta.objects.create(id_venta=id_venta,fecha=fecha,estado=estado,
    cantidad=cantidad,precio_total=precio_total,id_producto=id_producto,id_empleado=id_empleado,id_cliente=id_cliente)
    return redirect("venta")

def seleccionarVenta(request,id_venta):
    venta=Venta.objects.get(id_venta=id_venta)
    return render(request,"editarVenta.html",{"lasventas":venta})

def editarVenta(request):
    id_venta =request.POST["txtid_venta"]
    fecha =request.POST["datefecha"]
    estado  =request.POST["txtestado"]
    cantidad  =request.POST["numcantidad"] 
    precio_total  =request.POST["numprecio"]
    id_producto  =request.POST["txtid_producto"]
    id_empleado  =request.POST["txtid_empleado"]
    id_cliente  =request.POST["txtid_cliente"]
    venta=Venta.objects.get(id_venta=id_venta)
    venta.fecha=fecha
    venta.estado=estado
    venta.cantidad=cantidad
    venta.precio_total=precio_total
    venta.id_producto=id_producto
    venta.id_empleado=id_empleado
    venta.id_cliente=id_cliente
    venta.save()
    return redirect("venta")

def borrarVenta(request,id_venta):
    venta=Venta.objects.get(id_venta=id_venta)
    venta.delete()
    return redirect("venta")