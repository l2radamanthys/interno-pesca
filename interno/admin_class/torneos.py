from django.contrib import admin
from interno.models.torneos import Torneo


class TorneoAdmin(admin.ModelAdmin):
    model = Torneo
    list_display = (
        "id",
        "nombre",
    )
    search_fields = ("nombre",)
