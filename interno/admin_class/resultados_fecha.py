from django.contrib import admin
from interno.models.resultados_fecha import ResultadoFecha


class ResultadoFechaAdmin(admin.ModelAdmin):
    model = ResultadoFecha
    list_display = (
        'id',
        'participante',
    )
