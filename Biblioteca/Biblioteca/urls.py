from django.contrib import admin
from django.urls import path
from TrabajoFinal import views

urlpatterns = [
    path('', views.listar_bibliotecas, name='home'),
    path('bibliotecas/nombre/<str:nombre>/', views.buscar_biblioteca_por_nombre, name='buscar_biblioteca_por_nombre'),
    path('bibliotecas/ciudad/<str:ciudad>/', views.buscar_bibliotecas_por_ciudad, name='buscar_bibliotecas_por_ciudad'),
    path('bibliotecas/<int:biblioteca_id>/libros/', views.listar_libros_de_biblioteca, name='listar_libros_de_biblioteca'),
    path('bibliotecas/<int:biblioteca_id>/libros/titulo/<str:titulo>/', views.buscar_libro_por_titulo_de_biblioteca, name='buscar_libro_por_titulo_de_biblioteca'),
    path('bibliotecas/<int:biblioteca_id>/libros/autor/<str:autor>/', views.buscar_libro_por_autor_de_biblioteca, name='buscar_libro_por_autor_de_biblioteca'),
    path('bibliotecas/<int:biblioteca_id>/libros/editorial/<str:editorial>/', views.buscar_libro_por_editorial_de_biblioteca, name='buscar_libro_por_editorial_de_biblioteca'),
    path('libros/titulo/<str:titulo>/', views.buscar_libro_por_titulo, name='buscar_libro_por_titulo'),
    path('libros/titulo/<str:titulo>/disponibilidad/', views.buscar_libro_por_titulo_y_disponibilidad, name='buscar_libro_por_titulo_y_disponibilidad'),
]

