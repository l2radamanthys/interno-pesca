from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
# from rest_framework_json_api.relations import ResourceRelatedField

from interno.models.especies_por_fecha import EspeciePorFecha


class EspeciePorFechaSerializer(ModelSerializer):
    class Meta:
        model = EspeciePorFecha
        fields = (
            'id',
            'nombre',
        )

    # included_serializers = {
    #     'user': UserSerializer,
    # }
