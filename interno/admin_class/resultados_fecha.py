from django.contrib import admin
from interno.models.resultados_fecha import ResultadoFecha
from interno.models.especies_resultados import EspecieResultado


class EspecieResultadoInline(admin.TabularInline):
    model = EspecieResultado
    extra = 0


class ResultadoFechaAdmin(admin.ModelAdmin):
    model = ResultadoFecha
    list_display = (
        "id",
        "participante",
        "fecha_de_pesca",
        "puntaje_obtenido",
    )
    autocomplete_fields = ("participante",)
    inlines = (
        EspecieResultadoInline,
    )


