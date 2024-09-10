from django.db import models


class TypeAsociado(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return f'Tipo de asociado: {self.name}'

class TypesRiesgos(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return f'Riesgo nivel: {self.name}'

class Esecenarios(models.Model):
    name = models.CharField(max_length=200)
    salarioMin = models.CharField(max_length=200)
    salarioMax = models.CharField(max_length=200)

    def __srt__(self):
        return f'{self.name}'

class Rotativo(models.Model):
    escenario = models.ForeignKey(Esecenarios, on_delete=models.CASCADE)
    riesgo = models.ForeignKey(TypesRiesgos, on_delete=models.CASCADE)
    typeAsociado = models.ForeignKey(TypeAsociado, on_delete=models.CASCADE)
    scoreMin = models.IntegerField()
    scoreMax = models.IntegerField()
    EA = models.FloatField()
    NMV = models.FloatField()
    plazo = models.IntegerField()
