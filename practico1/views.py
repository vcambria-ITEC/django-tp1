from django.shortcuts import render
from .models import Clima

def bienvenida(request):
    return render(request, 'practico1/index.html')

def clima(request):
    climas = Clima.objects.all().order_by('-fecha_y_hora')
    context = {
        'climas': climas
    }
    return render(request, 'practico1/clima.html', context)