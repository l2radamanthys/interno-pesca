from django.http import HttpResponse
from django.template import loader
from interno.models.torneos import Torneo


def home_page(request):
    template = loader.get_template("home.html")
    context = {
        "torneos": Torneo.objects.all(),
    }
    return HttpResponse(template.render(context, request))


def detalle_torneo(request, pk):
    template = loader.get_template("detalle_torneo.html")
    torneo = Torneo.objects.get(pk=pk)
    context = {
        "torneo": torneo,
        "categorias": torneo.categorias.all(),
        "fechas_de_pesca": torneo.fechas_de_pesca.all(),
    }
    return HttpResponse(template.render(context, request))


def resultado_fecha_de_pesca(request, pk):
    template = loader.get_template("resultado_fecha_de_pesca.html")
    context = {
    }
    return HttpResponse(template.render(context, request))
