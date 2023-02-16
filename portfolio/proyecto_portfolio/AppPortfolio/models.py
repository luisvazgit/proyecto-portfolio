from django.db import models

# Create your models here.
class Mis_datos(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=40)
    mail = models.EmailField()


class Cursos(models.Model):
    nombre = models.CharField(max_length=50)
    institucion = models.CharField(max_length=50)
    fecha = models.IntegerField()

class Habilidades_blandas(models.Model):
    Habildad = models.CharField(max_length=300)


