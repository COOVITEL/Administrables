from django.db import models


class TasasCooviahorro(models.Model):
    type = models.CharField(max_length=100)
    amountMin = models.CharField(max_length=100)
    termMin = models.IntegerField()
    tasa = models.FloatField()
    
    def __str__(self):
        return self.type

