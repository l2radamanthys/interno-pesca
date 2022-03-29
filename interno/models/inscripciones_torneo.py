from django.db import models


class InscripcionTorneo(models.Model):
    participante = models.ForeignKey(
        "Participante",
        related_name="inscripciones_torneo",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True,
    )
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE, default=None, blank=True, null=True)

    class Meta:
        db_table = "inscripciones_torneo"
        ordering = ["categoria__torneo", "categoria__nombre"]
        verbose_name = "Inscripcion Torneo"
        verbose_name_plural = "inscripciones torneo"

    def __str__(self):
        return "Inscripcion Torneo"
