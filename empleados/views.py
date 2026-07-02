from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError
from .models import Cargo, Empleado
from .forms import CargoForm, EmpleadoForm

# Create your views here.

# ---- Cargos (VBF) ----

@login_required
def cargo_list(request):
    cargos = Cargo.objects.all()
    return render(request, 'empleados/vbf/cargo_list.html', {'cargos': cargos})


@login_required
def cargo_create(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cargo_list')
    else:
        form = CargoForm()
    return render(request, 'empleados/vbf/cargo_form.html', {'form': form})


@login_required
def cargo_update(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    if request.method == 'POST':
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('cargo_list')
    else:
        form = CargoForm(instance=cargo)
    return render(request, 'empleados/vbf/cargo_form.html', {'form': form, 'cargo': cargo})


@login_required
def cargo_delete(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    error = None
    if request.method == 'POST':
        try:
            cargo.delete()
            return redirect('cargo_list')
        except ProtectedError:
            error = 'No se puede eliminar el cargo porque tiene empleados asociados.'
    return render(request, 'empleados/vbf/cargo_confirm_delete.html', {'cargo': cargo, 'error': error})


# ---- Empleados (VBF) ----

@login_required
def empleado_list(request):
    empleados = Empleado.objects.select_related('cargo').all()
    return render(request, 'empleados/vbf/empleado_list.html', {'empleados': empleados})


@login_required
def empleado_create(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleado_list')
    else:
        form = EmpleadoForm()
    return render(request, 'empleados/vbf/empleado_form.html', {'form': form})


@login_required
def empleado_update(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleado_list')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleados/vbf/empleado_form.html', {'form': form, 'empleado': empleado})


@login_required
def empleado_delete(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('empleado_list')
    return render(request, 'empleados/vbf/empleado_confirm_delete.html', {'empleado': empleado})
