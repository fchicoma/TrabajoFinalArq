from django import forms
from .models import Biblioteca, Libro

class BibliotecaForm(forms.ModelForm):
    class Meta:
        model = Biblioteca
        fields = ['nombre', 'direccion', 'ciudad', 'horario_apertura', 'horario_cierre', 'fecha_fundacion', 'normas']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'sinopsis', 'ano_publicacion', 'editorial', 'isbn', 'numero_de_ejemplares', 'biblioteca']
