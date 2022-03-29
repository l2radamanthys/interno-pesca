from re import search
from django.contrib import admin
from interno.models.inscripciones_torneo import InscripcionTorneo


class InscripcionTorneoAdmin(admin.ModelAdmin):
    model = InscripcionTorneo
    list_display = (
        "id",
        "participante",
        "categoria",
    )
    search_fields = (
        "categoria__nombre",
        "categoria__torneo__nombre",
        "participante__nombre",
        "participante__apellido",
        "participante__dni",
    )
    autocomplete_fields = (
        "categoria",
        "participante",
    )