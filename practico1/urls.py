from django.urls import path
from . import views

urlpatterns = [
    path("", views.bienvenida, name="bienvenido"),
    path("clima/", views.clima, name="clima"),
    path("crearclima/", views.crear_clima, name="crear_clima"),
    path("editarclima/<int:id>/", views.editar_clima, name="editar_clima"),
    path("eliminarclima/<int:id>/", views.eliminar_clima, name="eliminar_clima"),
]