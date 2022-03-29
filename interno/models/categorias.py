from django.db import models


class Categoria(models.Model):
    torneo = models.ForeignKey(
        "Torneo",
        related_name="categorias",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True,
    )
    nombre = models.CharField(max_length=200, default=None, blank=True, null=True)

    class Meta:
        db_table = "categorias"
        verbose_name = "Categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return f"{self.nombre} ({self.torneo})"
