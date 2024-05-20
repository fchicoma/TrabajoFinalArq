from django.shortcuts import render,get_object_or_404, redirect
from .models import Biblioteca, Libro
from .forms import BibliotecaForm, LibroForm




# Listar bibliotecas
def listar_bibliotecas(request):
    bibliotecas = Biblioteca.objects.all()
    return render(request, 'listar_bibliotecas.html', {'bibliotecas': bibliotecas})
#http://localhost:8000/


# Buscar biblioteca por nombre
def buscar_biblioteca_por_nombre(request, nombre):
    bibliotecas = Biblioteca.objects.filter(nombre=nombre)
    return render(request, 'buscar_biblioteca_por_nombre.html', {'bibliotecas': bibliotecas, 'nombre':nombre})
#http://localhost:8000/bibliotecas/nombre/Zacut/


# Buscar bibliotecas por ciudad
def buscar_bibliotecas_por_ciudad(request, ciudad):
    bibliotecas = Biblioteca.objects.filter(ciudad=ciudad)
    return render(request, 'buscar_bibliotecas_por_ciudad.html', {'bibliotecas': bibliotecas, 'ciudad':ciudad})
#http://127.0.0.1:8000/bibliotecas/ciudad/Madrid/



# Listar libros de una biblioteca

def listar_libros_de_biblioteca(request, biblioteca_id):
    biblioteca = get_object_or_404(Biblioteca, id=biblioteca_id)
    libros = Libro.objects.filter(biblioteca=biblioteca)
    return render(request, 'listar_libros_de_biblioteca.html', {'libros': libros, 'biblioteca': biblioteca})
#http://127.0.0.1:8000/bibliotecas/1/libros/



# Buscar libro por título de una biblioteca
def buscar_libro_por_titulo_de_biblioteca(request, titulo, biblioteca_id):
    biblioteca = get_object_or_404(Biblioteca, id=biblioteca_id)
    libros = Libro.objects.filter(titulo=titulo, biblioteca_id=biblioteca_id)
    return render(request, 'buscar_libro_por_titulo_de_biblioteca.html', {'libros': libros, 'titulo':titulo, 'biblioteca':biblioteca})
#http://127.0.0.1:8000/bibliotecas/1/libros/titulo/Don%20Quijote/




# Buscar libro por autor de una biblioteca
def buscar_libro_por_autor_de_biblioteca(request, autor, biblioteca_id):
    biblioteca = get_object_or_404(Biblioteca, id=biblioteca_id)
    libros = Libro.objects.filter(autor__icontains=autor, biblioteca=biblioteca)
    return render(request, 'buscar_libro_por_autor_de_biblioteca.html', {'libros': libros, 'autor': autor, 'biblioteca': biblioteca})
#http://127.0.0.1:8000/bibliotecas/1/libros/autor/Cervantes/



# Buscar libro por editorial de una biblioteca
def buscar_libro_por_editorial_de_biblioteca(request, editorial, biblioteca_id):
    biblioteca = get_object_or_404(Biblioteca, id=biblioteca_id)
    libros = Libro.objects.filter(editorial__icontains=editorial, biblioteca=biblioteca)
    return render(request, 'buscar_libro_por_editorial_de_biblioteca.html', {'libros': libros, 'editorial': editorial, 'biblioteca': biblioteca})
#http://127.0.0.1:8000/bibliotecas/1/libros/editorial/Octaedro/




# Buscar libro por título
def buscar_libro_por_titulo(request, titulo):
    libros = Libro.objects.filter(titulo=titulo)
    return render(request, 'buscar_libro_por_titulo.html', {'libros': libros, 'titulo':titulo})
#http://127.0.0.1:8000/libros/titulo/Don%20Quijote/



# Buscar libro por título y disponibilidad
def buscar_libro_por_titulo_y_disponibilidad(request, titulo):
    libros = Libro.objects.filter(titulo=titulo, numero_de_ejemplares__gt=0)
    return render(request, 'buscar_libro_por_titulo_y_disponibilidad.html', {'libros': libros, 'titulo':titulo})
#http://localhost:8000/libros/titulo/Don%20Quijote/disponibilidad/



# Añadir nueva biblioteca
def añadir_biblioteca(request):
    if request.method == 'POST':
        form = BibliotecaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_bibliotecas')
    else:
        form = BibliotecaForm()
    return render(request, 'añadir_biblioteca.html', {'form': form})

# Añadir nuevo libro
def añadir_libro(request,biblioteca_id):
    biblioteca = get_object_or_404(Biblioteca, pk=biblioteca_id)
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.biblioteca = biblioteca
            libro.save()
            return redirect('listar_libros_de_biblioteca', biblioteca_id=biblioteca.id)
    else:
        form = LibroForm()
    return render(request, 'añadir_libro.html', {'form': form, 'biblioteca': biblioteca})

# Editar libro
def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros_de_biblioteca', biblioteca_id=libro.biblioteca.id)
    else:
        form = LibroForm(instance=libro)
    return render(request, 'editar_libro.html', {'form': form})

# Editar biblioteca
def editar_biblioteca(request, pk):
    biblioteca = get_object_or_404(Biblioteca, pk=pk)
    if request.method == 'POST':
        form = BibliotecaForm(request.POST, request.FILES, instance=biblioteca)
        if form.is_valid():
            form.save()
            return redirect('listar_bibliotecas')
    else:
        form = BibliotecaForm(instance=biblioteca)
    return render(request, 'editar_biblioteca.html', {'form': form})

# Borrar libro
def borrar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        biblioteca_id = libro.biblioteca.id
        libro.delete()
        return redirect('listar_libros_de_biblioteca', biblioteca_id=biblioteca_id)
    return render(request, 'borrar_libro.html', {'object': libro})

# Borrar biblioteca
def borrar_biblioteca(request, pk):
    biblioteca = get_object_or_404(Biblioteca, pk=pk)
    if request.method == 'POST':
        biblioteca.delete()
        return redirect('listar_bibliotecas')
    return render(request, 'borrar_biblioteca.html', {'object': biblioteca})