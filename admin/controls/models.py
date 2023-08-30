from django.db import models

class TasasCDAT(models.Model):
    since = models.IntegerField()
    until = models.IntegerField()
    amountsince = models.IntegerField()
    amountuntil = models.IntegerField()
    tasa = models.FloatField(max_length=20)
    
    def __str__(self):
        return f"Monto desde {self.since} hasta {self.until}, periodo entre {self.amountsince} y {self.amountuntil}"

class TasasCooviahorro(models.Model):
    type = models.CharField(max_length=100)
    amountMin = models.IntegerField()
    termMin = models.IntegerField()
    tasa = models.FloatField()
    
    def __str__(self):
        return self.type
