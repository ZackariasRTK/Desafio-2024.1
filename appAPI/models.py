from django.db import models


class acharIP(models.Model):

    ip = models.CharField(verbose_name="IP", max_length=50)
    cidade = models.CharField(verbose_name="Cidade", max_length=50, blank=True, null=True)
    regiao = models.CharField(verbose_name="Região", max_length=50, blank=True, null=True)
    paisC = models.CharField(verbose_name="Código do país", max_length=50, blank=True, null=True)
    paisN = models.CharField(verbose_name="Nome do país", max_length=50, blank=True, null=True)
    capital = models.CharField(verbose_name="Capital do país", max_length=50, blank=True, null=True)