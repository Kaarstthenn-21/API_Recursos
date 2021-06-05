from django.db import models

class RUC(models.Model):
    rucEmpresa= models.CharField(max_length=11, blank=False, null=False,unique=True)
    nombreEmpresa=models.CharField(max_length=50)
    estado=models.CharField(max_length=8)
    tipoEmpresa=models.CharField(max_length=50)
    rutaRUC=models.CharField(max_length=80)
    titular=models.CharField(max_length=50)
    identificacion=models.CharField(max_length=8,blank=False, null=False,unique=True)
