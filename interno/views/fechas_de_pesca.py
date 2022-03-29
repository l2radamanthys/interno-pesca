from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from interno.models.fechas_de_pesca import FechaDePesca
from interno.serializers.fechas_de_pesca import FechaDePescaSerializer


class FechaDePescaViewSet(viewsets.ModelViewSet):
    queryset = FechaDePesca.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = FechaDePescaSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
