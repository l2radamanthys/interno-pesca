from django.db import models


class FechaDePesca(models.Model):
    nombre = models.CharField(max_length=200, default=None, blank=True, null=True)
    lugar = models.CharField(max_length=200, default=None, blank=True, null=True)
    fecha = models.DateField(default=None, blank=True, null=True)
    torneo = models.ForeignKey('Torneo', related_name="fechas_de_pesca", on_delete=models.CASCADE, default=None, blank=True, null=True)
    orden = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        db_table = 'fechas_de_pesca'
        verbose_name = "Fecha de pesca"
        verbose_name_plural = "fechas de pesca"

    # def __str__(self):
    #     return self.nombre
