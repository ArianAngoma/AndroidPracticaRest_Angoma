from rest_framework import serializers
from .models import Solicitud


class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ('id', 'email', 'tipo', 'motivo', 'imagen')
