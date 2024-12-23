from django.db import models

class Sucursal(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class Asesores(models.Model):
    name = models.CharField(max_length=200)
    document = models.IntegerField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(auto_now_add=True)