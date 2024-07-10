from django.db import models

class TasasCDAT(models.Model):
    person = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    since = models.CharField(max_length=100)
    until = models.CharField(max_length=100)
    amountsince = models.IntegerField()
    amountuntil = models.IntegerField()
    tasa = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Monto desde {self.since} hasta {self.until}, periodo entre {self.amountsince} y {self.amountuntil}"

class TasasCooviahorro(models.Model):
    type = models.CharField(max_length=100)
    amountMin = models.CharField(max_length=100)
    termMin = models.IntegerField()
    tasa = models.CharField(max_length=100)
    
    def __str__(self):
        return self.type
