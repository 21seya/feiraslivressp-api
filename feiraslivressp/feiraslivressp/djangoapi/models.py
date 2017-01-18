from django.db import models


class Feiras(models.Model):
    # cod = models.IntegerField(read_only=True)
    # By default, Django gives each model the
    # id = models.AutoField(primary_key=True)
    longi = models.CharField(requerid=True, allow_blank=True, max_length=20)
    lat = models.CharField(requerid=True, allow_blank=True, max_length=20)
    setcens = models.IntegerField(requerid=True, allow_blank=True,
                                  max_length=20)
    areap = models.IntegerField(requerid=True, allow_blank=True, max_length=20)
    coddist = models.IntegerField(requerid=True, allow_blank=True,
                                  max_length=5)
    distrito = models.CharField(requerid=True, allow_blank=True, max_length=20)
    codsubpref = models.IntegerField(requerid=True, allow_blank=True,
                                     max_length=5)
    subprefe = models.CharField(requerid=True, allow_blank=True, max_length=50)
    regiao5 = models.CharField(requerid=True, allow_blank=True, max_length=20)
    regiao8 = models.CharField(requerid=True, allow_blank=True, max_length=20)
    nome_feira = models.CharField(requerid=True, allow_blank=True,
                                  max_length=50)
    registro = models.CharField(requerid=True, allow_blank=True, max_length=20)
    logradouro = models.CharField(requerid=True, allow_blank=True,
                                  max_length=50)
    numero = models.IntegerField(requerid=True, allow_blank=True, max_length=6)
    bairro = models.CharField(requerid=True, allow_blank=True, max_length=50)
    referencia = models.CharField(requerid=True, allow_blank=True,
                                  max_length=50)
