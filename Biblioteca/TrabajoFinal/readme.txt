- Para crear y activar entorno en Python

python3 -m venv env
source env/bin/activate






- Para instalar Django

pip install Django






- Para crear el proyecto y la aplicacion

TrabajoFinalArq % django-admin startproject Biblioteca
python manage.py startapp Biblioteca       
cd Biblioteca
python manage.py startapp TrabajoFinal





- Para clonar el repositorio de git

cd Desktop
git clone https://github.com/fchicoma/TrabajoFinalArq
cd TrabajoFinalArq
code .






- Para iniciar servidor desarrollo

python3 manage.py runserver







- Para comprobar rutas (Ejemplos vacíos)

Listar biblios: http://localhost:8000/
Biblio nombre: http://localhost:8000/bibliotecas/nombre/Biblioteca%20Central/
Biblio ciudad: http://localhost:8000/bibliotecas/ciudad/Madrid/
Libros biblio: http://localhost:8000/bibliotecas/1/libros/
Libro biblio: http://localhost:8000/bibliotecas/1/libros/titulo/El%20Principito/
Libro autor biblio: http://localhost:8000/bibliotecas/1/libros/autor/Gabriel%20Garc%C3%ADa%20M%C3%A1rquez/
Libro editorial biblio: http://localhost:8000/bibliotecas/1/libros/editorial/Alfaguara/
Libro titulo todas biblios: http://localhost:8000/libros/titulo/El%20Principito/
Libro titulo disponible todas biblios: http://localhost:8000/libros/titulo/El%20Principito/disponibilidad/



