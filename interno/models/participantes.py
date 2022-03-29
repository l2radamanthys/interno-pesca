from django.db import models


class Participante(models.Model):
    nombre = models.CharField(max_length=200, default=None, blank=True, null=True)
    apellido = models.CharField(max_length=200, default=None, blank=True, null=True)
    dni = models.CharField(max_length=200, default=None, blank=True, null=True)
    fecha_nacimiento = models.DateField(default=None, blank=True, null=True)

    class Meta:
        db_table = 'participantes'
        verbose_name = "Participante"
        verbose_name_plural = "participantes"

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
