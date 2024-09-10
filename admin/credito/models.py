from django.db import models


class TypeAsociado(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.name}"

class NoSociales(models.Model):
    name = models.CharField(max_length=200)
    usura = models.FloatField()
    descuentos = models.FloatField()
    techoEA = models.FloatField()
    techoNMV = models.FloatField()
    plazo = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} a un plazo de {self.plazo}"

class TasasNoSociales(models.Model):
    """"""
    perfil = models.ForeignKey(TypeAsociado, on_delete=models.CASCADE)
    maxScore = models.IntegerField()
    minScore = models.IntegerField()
    fg = models.FloatField()
    plazo = models.IntegerField()
    garantia = models.CharField(max_length=200)
    piso = models.FloatField()

class Fidelizacion(models.Model):
    """"""
    name = models.CharField(max_length=200)
    porcentaje = models.FloatField()
    tasa6 = models.FloatField()
    tasa12 = models.FloatField()
    tasa24 = models.FloatField()
    tasa36 = models.FloatField()
    tasa48 = models.FloatField()
    tasa60 = models.FloatField()
    tasa72 = models.FloatField()
    plazoMax = models.IntegerField()
    garantia = models.CharField(max_length=500)
    
    def __str__(self):
        return f"{self.name}"

class Sociales(models.Model):
    """"""
    name = models.CharField(max_length=200)
    tasa6 = models.FloatField()
    tasa12 = models.FloatField()
    tasa24 = models.FloatField()
    tasa36 = models.FloatField()
    tasa48 = models.FloatField(default=0)
    tasa60 = models.FloatField(default=0)
    tasa72 = models.FloatField(default=0)
    tasa84 = models.FloatField(default=0)
    plazoMax = models.IntegerField()
    
    def __str__(self):
        return f"{self.name}"

class AsociadoType(models.Model):
    """"""
    name = models.CharField(max_length=100)