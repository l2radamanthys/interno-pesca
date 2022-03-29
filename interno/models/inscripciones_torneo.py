from django.db import models


class InscripcionTorneo(models.Model):
    torneo = models.ForeignKey("Torneo", related_name="inscripciones_torneo", on_delete=models.CASCADE, default=None, blank=True, null=True)
    participante = models.ForeignKey("Participante", related_name="inscripciones_torneo", on_delete=models.CASCADE, default=None, blank=True, null=True)

    class Meta:
        db_table = 'inscripciones_torneo'
        verbose_name = "Inscripcion Torneo"
        verbose_name_plural = "inscripciones torneo"

    def __str__(self):
        return "Inscripcion Torneo"
