from django.contrib import admin
from interno.models.especies_por_fecha import EspeciePorFecha


class EspeciePorFechaAdmin(admin.ModelAdmin):
    model = EspeciePorFecha
    list_display = (
        'id',
        'fecha_de_pesca',
        'especie',
        'puntaje',
    )

