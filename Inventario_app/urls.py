from django.urls import path 
from Inventario_app import views

urlpatterns = [
    path("inventario",views.inicio_vista, name="inventario"),
    path("registrarInventario/",views.registrarInventario,name="registrarInventario"),
    path("seleccionarInventario/<id_inventario>",views.seleccionarInventario,name="seleccionarInventario"),
    path("editarInventario/",views.editarInventario,name="editarInventario"),
    path("borrarInventario/<id_inventario>",views.borrarInventario,name="borrarInventario")
]