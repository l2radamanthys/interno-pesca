from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from interno.models.participantes import Participante
from interno.serializers.participantes import ParticipanteSerializer


class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ParticipanteSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
