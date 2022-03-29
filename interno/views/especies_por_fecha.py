from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from interno.models.especies_por_fecha import EspeciePorFecha
from interno.serializers.especies_por_fecha import EspeciePorFechaSerializer


class EspeciePorFechaViewSet(viewsets.ModelViewSet):
    queryset = EspeciePorFecha.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = EspeciePorFechaSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
