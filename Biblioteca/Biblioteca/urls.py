from django.contrib import admin
from django.urls import path
from TrabajoFinal import views

urlpatterns = [
    path('', views.listar_bibliotecas, name='listar_bibliotecas'),
    path('bibliotecas/nombre/<str:nombre>/', views.buscar_biblioteca_por_nombre, name='buscar_biblioteca_por_nombre'),
    path('bibliotecas/ciudad/<str:ciudad>/', views.buscar_bibliotecas_por_ciudad, name='buscar_bibliotecas_por_ciudad'),
    path('bibliotecas/<int:biblioteca_id>/libros/', views.listar_libros_de_biblioteca, name='listar_libros_de_biblioteca'),
    path('bibliotecas/<int:biblioteca_id>/libros/titulo/<str:titulo>/', views.buscar_libro_por_titulo_de_biblioteca, name='buscar_libro_por_titulo_de_biblioteca'),
    path('bibliotecas/<int:biblioteca_id>/libros/autor/<str:autor>/', views.buscar_libro_por_autor_de_biblioteca, name='buscar_libro_por_autor_de_biblioteca'),
    path('bibliotecas/<int:biblioteca_id>/libros/editorial/<str:editorial>/', views.buscar_libro_por_editorial_de_biblioteca, name='buscar_libro_por_editorial_de_biblioteca'),
    path('libros/titulo/<str:titulo>/', views.buscar_libro_por_titulo, name='buscar_libro_por_titulo'),
    path('libros/titulo/<str:titulo>/disponibilidad/', views.buscar_libro_por_titulo_y_disponibilidad, name='buscar_libro_por_titulo_y_disponibilidad'),
    path('biblioteca/nueva/', views.añadir_biblioteca, name='añadir_biblioteca'),
    path('biblioteca/editar/<int:pk>/', views.editar_biblioteca, name='editar_biblioteca'),
    path('biblioteca/eliminar/<int:pk>/', views.borrar_biblioteca, name='borrar_biblioteca'),
    path('biblioteca/<int:biblioteca_id>/libro/nuevo/', views.añadir_libro, name='añadir_libro'),
    path('biblioteca/libro/editar/<int:pk>/', views.editar_libro, name='editar_libro'),
    path('biblioteca/libro/eliminar/<int:pk>/', views.borrar_libro, name='borrar_libro'),
]

