from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from interno.models.especies_resultados import EspecieResultado
from interno.serializers.especies_resultados import EspecieResultadoSerializer


class EspecieResultadoViewSet(viewsets.ModelViewSet):
    queryset = EspecieResultado.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = EspecieResultadoSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
