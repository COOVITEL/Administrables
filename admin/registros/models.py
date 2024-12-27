from django.db import models

class RegistrosSimulacionesCreditos(models.Model):
    name = models.CharField(max_length=100)
    document = models.IntegerField()
    dateborn = models.CharField(max_length=100)
    dateafi = models.CharField(max_length=100)
    typeAsociado = models.CharField(max_length=100)
    typeContract = models.CharField(max_length=100, null=True, blank=True)
    seniority = models.CharField(max_length=100, null=True, blank=True)
    payForm = models.CharField(max_length=100)
    score = models.IntegerField()
    warranty = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    others = models.CharField(max_length=100)
    cuotasDes = models.CharField(max_length=100)
    cuotasCen = models.CharField(max_length=100)
    cooviahorro = models.CharField(max_length=100)
    cdat = models.CharField(max_length=100)
    aportes = models.CharField(max_length=100)
    credit = models.CharField(max_length=100)
    cuotas = models.CharField(max_length=100)
    monto = models.CharField(max_length=100)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    createdBy = models.CharField(max_length=200, null=True, blank=True)

class RegistroSimulacionesCdat(models.Model):
    nameAsociado = models.CharField(max_length=100)
    typeCdat = models.CharField(max_length=100)
    tasa = models.FloatField()
    value = models.CharField(max_length=100)
    plazo = models.IntegerField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    createdBy = models.CharField(max_length=100)

class RegistroSimulacionRotativo(models.Model):
    nameAsociado = models.CharField(max_length=100)
    document = models.IntegerField()
    dateAfiliacion = models.CharField(max_length=100)
    typeAsociado = models.CharField(max_length=100)
    typeContract = models.CharField(max_length=100, null=True, blank=True)
    pagaduria = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    descuentos = models.CharField(max_length=100)
    score = models.IntegerField()
    monto = models.CharField(max_length=100)

class RegistroSimulacionCooviahorro(models.Model):
    pass