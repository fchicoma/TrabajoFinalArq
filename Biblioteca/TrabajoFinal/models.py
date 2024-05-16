from django.db import models

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()
    fecha_fundacion = models.DateField()
    normas = models.FileField(upload_to='normas/', null=True, blank=True)

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    sinopsis = models.TextField()
    ano_publicacion = models.DateField()
    editorial = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    numero_de_ejemplares = models.IntegerField()
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
