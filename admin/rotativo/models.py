from django.db import models

class AsociadoRotativo(models.Model):
    name = models.CharField(max_length=100)
    montoMax = models.CharField(max_length=200)
    plazoMax = models.IntegerField()
    requisitos = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}"

class Escenarios(models.Model):
    name = models.CharField(max_length=200)
    salarioMin = models.CharField(max_length=200)
    salarioMax = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

class Rotativo(models.Model):
    escenario = models.ForeignKey(Escenarios, on_delete=models.CASCADE)
    typeAsociado = models.ForeignKey(AsociadoRotativo, on_delete=models.CASCADE)

    riesgo = models.CharField(max_length=200)
    scoreMin = models.IntegerField()
    scoreMax = models.IntegerField(blank=True, null=True)
    EA = models.FloatField()
    NMV = models.FloatField()
    plazo = models.IntegerField()
