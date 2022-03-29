from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
# from rest_framework_json_api.relations import ResourceRelatedField

from interno.models.resultados_fecha import ResultadoFecha


class ResultadoFechaSerializer(ModelSerializer):
    class Meta:
        model = ResultadoFecha
        fields = (
            'id',
            'nombre',
        )

    # included_serializers = {
    #     'user': UserSerializer,
    # }
