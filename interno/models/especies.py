from django.db import models


class Especie(models.Model):
    nombre = models.CharField(max_length=200, default=None, blank=True, null=True)

    class Meta:
        db_table = 'especies'
        verbose_name = "Especie"
        verbose_name_plural = "especies"

    def __str__(self):
        return self.nombre
