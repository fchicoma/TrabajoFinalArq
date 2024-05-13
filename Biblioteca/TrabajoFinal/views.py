from django.shortcuts import render

from django.shortcuts import render
from .models import Biblioteca, Libro

# Listar bibliotecas
def listar_bibliotecas(request):
    bibliotecas = Biblioteca.objects.all()
    return render(request, 'listar_bibliotecas.html', {'bibliotecas': bibliotecas})

# Buscar biblioteca por nombre
def buscar_biblioteca_por_nombre(request, nombre):
    bibliotecas = Biblioteca.objects.filter(nombre=nombre)
    return render(request, 'buscar_biblioteca_por_nombre.html', {'bibliotecas': bibliotecas})

# Buscar bibliotecas por ciudad
def buscar_bibliotecas_por_ciudad(request, ciudad):
    bibliotecas = Biblioteca.objects.filter(ciudad=ciudad)
    return render(request, 'buscar_bibliotecas_por_ciudad.html', {'bibliotecas': bibliotecas})

# Listar libros de una biblioteca
def listar_libros_de_biblioteca(request, biblioteca_id):
    libros = Libro.objects.filter(biblioteca_id=biblioteca_id)
    return render(request, 'listar_libros_de_biblioteca.html', {'libros': libros})

# Buscar libro por título de una biblioteca
def buscar_libro_por_titulo_de_biblioteca(request, titulo, biblioteca_id):
    libros = Libro.objects.filter(titulo=titulo, biblioteca_id=biblioteca_id)
    return render(request, 'buscar_libro_por_titulo_de_biblioteca.html', {'libros': libros})

# Buscar libro por autor de una biblioteca
def buscar_libro_por_autor_de_biblioteca(request, autor, biblioteca_id):
    libros = Libro.objects.filter(autor=autor, biblioteca_id=biblioteca_id)
    return render(request, 'buscar_libro_por_autor_de_biblioteca.html', {'libros': libros})

# Buscar libro por editorial de una biblioteca
def buscar_libro_por_editorial_de_biblioteca(request, editorial, biblioteca_id):
    libros = Libro.objects.filter(editorial=editorial, biblioteca_id=biblioteca_id)
    return render(request, 'buscar_libro_por_editorial_de_biblioteca.html', {'libros': libros})

# Buscar libro por título
def buscar_libro_por_titulo(request, titulo):
    libros = Libro.objects.filter(titulo=titulo)
    return render(request, 'buscar_libro_por_titulo.html', {'libros': libros})

# Buscar libro por título y disponibilidad
def buscar_libro_por_titulo_y_disponibilidad(request, titulo):
    libros = Libro.objects.filter(titulo=titulo, numero_ejemplares__gt=0)
    return render(request, 'buscar_libro_por_titulo_y_disponibilidad.html', {'libros': libros})

