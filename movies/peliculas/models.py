from django.db import models

# Create your models here.
class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    lanzamiento = models.PositiveIntegerField()
    duracion = models.CharField(max_length=255)
    sinopsis = models.TextField()

    def __str__(self):
        return self.titulo, self.director, self.genero, self.lanzamiento, self.duracion, self.sinopsis