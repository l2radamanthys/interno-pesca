from django.contrib import admin
from interno.models.especies_resultados import EspecieResultado


class EspecieResultadoAdmin(admin.ModelAdmin):
    model = EspecieResultado
    list_display = (
        "id",
        "especie",
    )
