from django.shortcuts import render

def bienvenida(request):
    return render(request, 'practico1/index.html')

def clima(request):
    return render(request, 'practico1/clima.html')