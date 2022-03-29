from ast import mod
from django.db import models


class Torneo(models.Model):
    nombre = models.CharField(max_length=200, default=None, blank=True, null=True)

    class Meta:
        db_table = "torneos"
        verbose_name = "Torneo"
        verbose_name_plural = "torneos"

    def __str__(self):
        return self.nombre
