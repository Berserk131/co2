from django.shortcuts import render
from .models import ProductoTecnologico

def lista_productos(request):
    productos = ProductoTecnologico.objects.all()
    return render(request, 'calculadora/lista_productos.html', {'productos': productos})
