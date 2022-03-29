from django.contrib import admin
from interno.models.fechas_de_pesca import FechaDePesca
from interno.models.especies_por_fecha import EspeciePorFecha


class EspeciePorFechaInline(admin.TabularInline):
    model = EspeciePorFecha
    extra = 0


class FechaDePescaAdmin(admin.ModelAdmin):
    model = FechaDePesca
    list_display = (
        "id",
        "orden",
        "torneo",
        "nombre",
        "fecha",
    )
    inlines = [
        EspeciePorFechaInline,
    ]