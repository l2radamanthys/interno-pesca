from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from interno.models.resultados_fecha import ResultadoFecha
from interno.serializers.resultados_fecha import ResultadoFechaSerializer


class ResultadoFechaViewSet(viewsets.ModelViewSet):
    queryset = ResultadoFecha.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ResultadoFechaSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
