from django.db import models

from interno.models.fechas_de_pesca import FechaDePesca


class ResultadoFecha(models.Model):
    participante = models.ForeignKey(
        "Participante",
        related_name="resultados_fecha",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True,
    )
    fecha_de_pesca = models.ForeignKey(
        "FechaDePesca",
        related_name="resultados_fecha",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True,
    )
    hora_cupo = models.TimeField(default=None, blank=True, null=True)
    pieza_mayor = models.FloatField(default=0, blank=True, null=True)
    puntaje_obtenido = models.FloatField(default=0, blank=True, null=True)

    class Meta:
        db_table = "resultados_fecha"
        verbose_name = "Resultado fecha"
        verbose_name_plural = "resultados fecha"

    # def __str__(self):
    #     return self.nombre
