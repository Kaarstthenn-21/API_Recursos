from django.db import models

# Create your models here.
class DNI(models.Model):

    dni = models.CharField( unique=True , max_length=7)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField( max_length=50)

