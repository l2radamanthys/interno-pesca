from django.contrib import admin
from interno.models.fechas_de_pesca import FechaDePesca


class FechaDePescaAdmin(admin.ModelAdmin):
    model = FechaDePesca
    list_display = (
        'id',
        'torneo',
        'nombre',
        'fecha',
    )

