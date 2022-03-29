from django.db import models


class EspeciePorFecha(models.Model):
    fecha_de_pesca = models.ForeignKey(
        "FechaDePesca",
        related_name="especies_por_fecha",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True,
    )
    especie = models.ForeignKey(
        "Especie",
        related_name="especies_por_fecha",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True,
    )
    puntaje = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        db_table = "especies_por_fecha"
        verbose_name = "EspeciePorFecha"
        verbose_name_plural = "especies_por_fecha"

    # def __str__(self):
    #     return self.nombre
