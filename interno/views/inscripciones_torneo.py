from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from interno.models.inscripciones_torneo import InscripcionTorne
from interno.serializers.inscripciones_torneo import InscripcionTorneSerializer


class InscripcionTorneViewSet(viewsets.ModelViewSet):
    queryset = InscripcionTorne.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = InscripcionTorneSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
