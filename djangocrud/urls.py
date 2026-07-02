"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
from empleados import views as empleados_views
from empleados import views_cbv as empleados_cbv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),

    # Cargos - Vistas Basadas en Funciones (VBF)
    path('cargos/', empleados_views.cargo_list, name='cargo_list'),
    path('cargos/nuevo/', empleados_views.cargo_create, name='cargo_create'),
    path('cargos/<int:pk>/editar/', empleados_views.cargo_update, name='cargo_update'),
    path('cargos/<int:pk>/eliminar/', empleados_views.cargo_delete, name='cargo_delete'),

    # Empleados - Vistas Basadas en Funciones (VBF)
    path('empleados/', empleados_views.empleado_list, name='empleado_list'),
    path('empleados/nuevo/', empleados_views.empleado_create, name='empleado_create'),
    path('empleados/<int:pk>/editar/', empleados_views.empleado_update, name='empleado_update'),
    path('empleados/<int:pk>/eliminar/', empleados_views.empleado_delete, name='empleado_delete'),

    # Cargos - Vistas Basadas en Clases (VBC)
    path('cbv/cargos/', empleados_cbv.CargoListView.as_view(), name='cargo_list_cbv'),
    path('cbv/cargos/nuevo/', empleados_cbv.CargoCreateView.as_view(), name='cargo_create_cbv'),
    path('cbv/cargos/<int:pk>/editar/', empleados_cbv.CargoUpdateView.as_view(), name='cargo_update_cbv'),
    path('cbv/cargos/<int:pk>/eliminar/', empleados_cbv.CargoDeleteView.as_view(), name='cargo_delete_cbv'),

    # Empleados - Vistas Basadas en Clases (VBC)
    path('cbv/empleados/', empleados_cbv.EmpleadoListView.as_view(), name='empleado_list_cbv'),
    path('cbv/empleados/nuevo/', empleados_cbv.EmpleadoCreateView.as_view(), name='empleado_create_cbv'),
    path('cbv/empleados/<int:pk>/editar/', empleados_cbv.EmpleadoUpdateView.as_view(), name='empleado_update_cbv'),
    path('cbv/empleados/<int:pk>/eliminar/', empleados_cbv.EmpleadoDeleteView.as_view(), name='empleado_delete_cbv'),
]
