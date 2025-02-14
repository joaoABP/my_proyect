from django.shortcuts import render, redirect
from .forms import MedicamentoForm, ClienteForm, VentaForm
from .models import Medicamento

def index(request):
    return render(request, 'blog/index.html')

def crear_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MedicamentoForm()
    return render(request, 'blog/medicamento_form.html', {'form': form})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClienteForm()
    return render(request, 'blog/cliente_form.html', {'form': form})

def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VentaForm()
    return render(request, 'blog/venta_form.html', {'form': form})

def buscar_medicamento(request):
    query = request.GET.get('q')
    resultados = Medicamento.objects.filter(nombre__icontains=query) if query else []
    return render(request, 'blog/search_results.html', {'resultados': resultados, 'query': query})
