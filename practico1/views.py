from django.shortcuts import render, redirect, get_object_or_404
from .models import Clima, Ciudad
from .forms import ClimaForm

def bienvenida(request):
    return render(request, 'practico1/index.html')

def clima(request):
    climas = Clima.objects.all().order_by('-fecha_y_hora')
    context = {
        'climas': climas
    }
    return render(request, 'practico1/clima.html', context)

def crear_clima(request):
    if request.method == "POST":
        form = ClimaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clima")
    else:
        form = ClimaForm()

    return render(request, "practico1/crear_clima.html", {"form": form})

def editar_clima(request, id):

    clima = get_object_or_404(CLima, id=id)

    if request.method == "POST":
        form = ClimaForm(request.POST, instance=clima)
        if form.is_valid():
            form.save()
            return redirect("clima")
    else:
        form = CLimaForm(instance=clima)

    return render(request, "practico1/editar_clima.html", {"form": form})

def eliminar_clima(request, id):

    clima = get_object_or_404(Clima, id=id)

    if request.method == "POST":
        clima.activo = False
        clima.save()

        return redirect("clima")

    return render(request, "practico1/borrar_clima.html", {"clima": clima})