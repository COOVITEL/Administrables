from django.db import models

class TasasCDAT(models.Model):
    person = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    since = models.CharField(max_length=100)
    until = models.CharField(max_length=100)
    amountsince = models.IntegerField()
    amountuntil = models.IntegerField()
    tasa = models.FloatField()
    
    def __str__(self):
        return f"Monto desde {self.since} hasta {self.until}, periodo entre {self.amountsince} y {self.amountuntil}"

class TasasCooviahorro(models.Model):
    type = models.CharField(max_length=100)
    amountMin = models.CharField(max_length=100)
    termMin = models.IntegerField()
    tasa = models.FloatField()
    
    def __str__(self):
        return self.type

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