from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from interno.models.torneos import Torneo
from interno.serializers.torneos import TorneoSerializer


class TorneoViewSet(viewsets.ModelViewSet):
    queryset = Torneo.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = TorneoSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
