from django.contrib import admin

# Register your models here.
from interno.admin_class.torneos import Torneo, TorneoAdmin
from interno.admin_class.categorias import Categoria, CategoriaAdmin
from interno.admin_class.fechas_de_pesca import FechaDePesca, FechaDePescaAdmin
from interno.admin_class.especies_por_fecha import EspeciePorFecha, EspeciePorFechaAdmin
from interno.admin_class.especies_resultados import (
    EspecieResultado,
    EspecieResultadoAdmin,
)
from interno.admin_class.participantes import Participante, ParticipanteAdmin
from interno.admin_class.resultados_fecha import ResultadoFecha, ResultadoFechaAdmin
from interno.admin_class.inscripciones_torneo import (
    InscripcionTorneo,
    InscripcionTorneoAdmin,
)
from interno.admin_class.especies import Especie, EspecieAdmin


admin.site.register(Torneo, TorneoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(FechaDePesca, FechaDePescaAdmin)
admin.site.register(EspeciePorFecha, EspeciePorFechaAdmin)
admin.site.register(EspecieResultado, EspecieResultadoAdmin)
admin.site.register(Participante, ParticipanteAdmin)
admin.site.register(ResultadoFecha, ResultadoFechaAdmin)
admin.site.register(InscripcionTorneo, InscripcionTorneoAdmin)
admin.site.register(Especie, EspecieAdmin)
