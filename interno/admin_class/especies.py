from django.contrib import admin
from interno.models.especies import Especie


class EspecieAdmin(admin.ModelAdmin):
    model = Especie
    list_display = (
        "id",
        "nombre",
    )
