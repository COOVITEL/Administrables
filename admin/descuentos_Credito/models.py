from django.db import models
from credito.models import TypeAsociado

class MaximoAjuste(models.Model):
    """"""
    name = models.CharField(max_length=100, unique=True)
    value = models.IntegerField()

class AjustesScore(models.Model):
    """"""
    asociado = models.ForeignKey(TypeAsociado, on_delete=models.CASCADE)
    scoreMin = models.IntegerField()
    scoreMax = models.IntegerField()
    ajuste = models.IntegerField()
    
class AjustesAportes(models.Model):
    """"""
    asociado = models.ForeignKey(TypeAsociado, on_delete=models.CASCADE)
    aporteMin = models.CharField(max_length=200)
    aporteMax = models.CharField(max_length=200)
    ajuste = models.IntegerField()

class AjustesPlazo(models.Model):
    """"""
    asociado = models.ForeignKey(TypeAsociado, on_delete=models.CASCADE)
    plazoMin = models.IntegerField()
    plazoMax = models.IntegerField()
    ajuste = models.IntegerField()

class AjustesCDAT(models.Model):
    """"""
    montoMin = models.CharField(max_length=300)
    montoMax = models.CharField(max_length=300)
    ajuste = models.IntegerField()

class AjustesCooviahorro(models.Model):
    """"""
    montoMin = models.CharField(max_length=300)
    montoMax = models.CharField(max_length=300)
    ajuste = models.IntegerField()