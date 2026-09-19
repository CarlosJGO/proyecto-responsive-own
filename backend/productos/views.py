from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProveedorForm, CategoriaForm, ClienteForm
from .models import Categoria, Producto, Proveedor, Cliente

from .serializers import CategoriaSerializer, ProductoSerializer

#las views son las funciones que se llaman cuando se llama a una url
#las views se llaman desde el archivo urls.py

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['categoria', 'activo']
    search_fields = ['nombre', 'descripcion']


@api_view(['GET'])
def health_check(request):
    return Response({'status': 'ok', 'app': 'ferreteria-backend'})

##########################################################proveedores
def proveedor_list(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor_list.html', {'proveedores': proveedores})
#post encripta la info que se manda en una url. metodo mas seguro porque no manda la info en la url. get manda la info en la url y es menos seguro
def proveedor_create(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedor_list')
    else:
        form = ProveedorForm()
    return render(request, 'proveedor_form.html', {'form': form})
#el get se puede usar para visualizar otras cosas como una imagen

def proveedor_update(request, pk):
    proveedor_instance = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor_instance)
        if form.is_valid():
            form.save()
            return redirect('proveedor_list')
    else:
        form = ProveedorForm(instance=proveedor_instance)
    return render(request, 'proveedor_form.html', {'form': form})

def proveedor_delete(request, pk):
    proveedor_instance = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor_instance.delete()
        return redirect('proveedor_list')
    return render(request, 'proveedor_confirm_delete.html', {'proveedor': proveedor_instance})

##########################################################categorias
def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/categoria_list.html', {'categorias': categorias})

def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/categoria_form.html', {'form': form})

def categoria_update(request, pk):
    categoria_instance = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria_instance)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm(instance=categoria_instance)
    return render(request, 'categorias/categoria_form.html', {'form': form})

def categoria_delete(request, pk):
    categoria_instance = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria_instance.delete()
        return redirect('categoria_list')
    return render(request, 'categorias/categoria_confirm_delete.html', {'categoria': categoria_instance})


##########################################################clientes
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cliente_form.html', {'form': form})

def cliente_update(request, pk):
    cliente_instance = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente_instance)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente_instance)
    return render(request, 'clientes/cliente_form.html', {'form': form})

def cliente_delete(request, pk):
    cliente_instance = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente_instance.delete()
        return redirect('cliente_list')
    return render(request, 'clientes/cliente_confirm_delete.html', {'cliente': cliente_instance})