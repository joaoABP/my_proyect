from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('medicamento/', views.crear_medicamento, name='crear_medicamento'),
    path('cliente/', views.crear_cliente, name='crear_cliente'),
    path('venta/', views.crear_venta, name='crear_venta'),
    path('buscar/', views.buscar_medicamento, name='buscar_medicamento'),
]
