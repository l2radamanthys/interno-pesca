from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

# from rest_framework_json_api.relations import ResourceRelatedField

from interno.models.fechas_de_pesca import FechaDePesca


class FechaDePescaSerializer(ModelSerializer):
    class Meta:
        model = FechaDePesca
        fields = (
            "id",
            "nombre",
        )

    # included_serializers = {
    #     'user': UserSerializer,
    # }
