from django.contrib import admin
from interno.models.categorias import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    model = Categoria
    list_display = (
        "id",
        "torneo",
        "nombre",
    )
    search_fields = (
        "torneo__nombre",
        "nombre",
    )
