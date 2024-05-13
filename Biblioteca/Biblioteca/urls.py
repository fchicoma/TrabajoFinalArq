"""
URL configuration for Biblioteca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('bibliotecas/', views.listar_bibliotecas, name='listar_bibliotecas'),
    path('bibliotecas/nombre/<str:nombre>/', views.buscar_biblioteca_por_nombre, name='buscar_biblioteca_por_nombre'),
    path('bibliotecas/ciudad/<str:ciudad>/', views.buscar_bibliotecas_por_ciudad, name='buscar_bibliotecas_por_ciudad'),
    path('bibliotecas/<int:biblioteca_id>/libros/', views.listar_libros_de_biblioteca, name='listar_libros_de_biblioteca'),
    path('bibliotecas/<int:biblioteca_id>/libros/titulo/<str:titulo>/', views.buscar_libro_por_titulo_de_biblioteca, name='buscar_libro_por_titulo_de_biblioteca'),
    path('bibliotecas/<int:biblioteca_id>/libros/autor/<str:autor>/', views.buscar_libro_por_autor_de_biblioteca, name='buscar_libro_por_autor_de_biblioteca'),
    path('bibliotecas/<int:biblioteca_id>/libros/editorial/<str:editorial>/', views.buscar_libro_por_editorial_de_biblioteca, name='buscar_libro_por_editorial_de_biblioteca'),
    path('libros/titulo/<str:titulo>/', views.buscar_libro_por_titulo, name='buscar_libro_por_titulo'),
    path('libros/titulo/<str:titulo>/disponibilidad/', views.buscar_libro_por_titulo_y_disponibilidad, name='buscar_libro_por_titulo_y_disponibilidad'),
]

