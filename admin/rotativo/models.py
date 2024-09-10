from django.db import models


class Escenarios(models.Model):
    name = models.CharField(max_length=200)
    salarioMin = models.CharField(max_length=200)
    salarioMax = models.CharField(max_length=200)

    def __srt__(self):
        return f'{self.name}'

class Rotativo(models.Model):
    escenario = models.ForeignKey(Escenarios, on_delete=models.CASCADE)
    riesgo = models.CharField(max_length=200)
    typeAsociado = models.CharField(max_length=200)
    scoreMin = models.IntegerField()
    scoreMax = models.IntegerField()
    EA = models.FloatField()
    NMV = models.FloatField()
    plazo = models.IntegerField()
