from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Producto
from .forms import ProductoForm

def index(request):
    productos = Producto.objects.all()
    return render(request, 'app_producto/index.html', {'productos': productos})

def add(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'app_producto/add.html', {'form': ProductoForm(), 'success': True})
    else:
        form = ProductoForm()
    return render(request, 'app_producto/add.html', {'form': form})

def edit(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return render(request, 'app_producto/edit.html', {'form': form, 'success': True})
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'app_producto/edit.html', {'form': form})

def delete(request, id):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, pk=id)
        producto.delete()
    return HttpResponseRedirect(reverse('index'))
