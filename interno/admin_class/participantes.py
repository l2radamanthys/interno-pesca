from django.contrib import admin
from interno.models.participantes import Participante


class ParticipanteAdmin(admin.ModelAdmin):
    model = Participante
    list_display = (
        "id",
        "apellido",
        "nombre",
        "dni",
        "fecha_nacimiento",
    )
    search_fields = ("nombre", "apellido", "dni",)