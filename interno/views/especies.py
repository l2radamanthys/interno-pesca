from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from interno.models.especies import Especie
from interno.serializers.especies import EspecieSerializer


class EspecieViewSet(viewsets.ModelViewSet):
    queryset = Especie.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = EspecieSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
