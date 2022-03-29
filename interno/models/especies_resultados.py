from statistics import mode
from django.db import models


class EspecieResultado(models.Model):
    resultado_fecha = models.ForeignKey("ResultadoFecha", related_name="especies_resultados", on_delete=models.CASCADE, default=None, blank=True, null=True)
    especie = models.ForeignKey("Especie", related_name="especies_resultados", on_delete=models.CASCADE, default=None, blank=True, null=True)
    cantidad = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        db_table = 'especies_resultados'
        verbose_name = "EspecieResultado"
        verbose_name_plural = "especies_resultados"

    # def __str__(self):
    #     return self.nombre
