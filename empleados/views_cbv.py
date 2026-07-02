from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cargo, Empleado
from .forms import CargoForm, EmpleadoForm

# ---- Cargos (VBC) ----

class CargoListView(LoginRequiredMixin, ListView):
    model = Cargo
    template_name = 'empleados/vbc/cargo_list.html'
    context_object_name = 'cargos'


class CargoCreateView(LoginRequiredMixin, CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'empleados/vbc/cargo_form.html'
    success_url = reverse_lazy('cargo_list_cbv')


class CargoUpdateView(LoginRequiredMixin, UpdateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'empleados/vbc/cargo_form.html'
    success_url = reverse_lazy('cargo_list_cbv')


class CargoDeleteView(LoginRequiredMixin, DeleteView):
    model = Cargo
    template_name = 'empleados/vbc/cargo_confirm_delete.html'
    success_url = reverse_lazy('cargo_list_cbv')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            return redirect(self.success_url)
        except ProtectedError:
            return render(request, self.template_name, {
                'cargo': self.object,
                'object': self.object,
                'error': 'No se puede eliminar el cargo porque tiene empleados asociados.',
            })


# ---- Empleados (VBC) ----

class EmpleadoListView(LoginRequiredMixin, ListView):
    model = Empleado
    template_name = 'empleados/vbc/empleado_list.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        return Empleado.objects.select_related('cargo').all()


class EmpleadoCreateView(LoginRequiredMixin, CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/vbc/empleado_form.html'
    success_url = reverse_lazy('empleado_list_cbv')


class EmpleadoUpdateView(LoginRequiredMixin, UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/vbc/empleado_form.html'
    success_url = reverse_lazy('empleado_list_cbv')


class EmpleadoDeleteView(LoginRequiredMixin, DeleteView):
    model = Empleado
    template_name = 'empleados/vbc/empleado_confirm_delete.html'
    success_url = reverse_lazy('empleado_list_cbv')
