from django.urls import path
from . import views

urlpatterns = [
    path("", views.bienvenida, name="bienvenido"),
    path("clima/", views.clima, name="clima"),
]