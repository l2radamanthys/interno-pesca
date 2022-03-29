from django.contrib import admin
from interno.models.inscripciones_torneo import InscripcionTorneo


class InscripcionTorneoAdmin(admin.ModelAdmin):
    model = InscripcionTorneo
    list_display = (
        'id',
        'participante',
    )

