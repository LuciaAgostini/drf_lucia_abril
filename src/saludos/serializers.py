from rest_framework import serializers

from .models import Saludo


class SaludoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saludo
        fields = ["id", "mensaje", "autor", "idioma", "creado"]
        read_only_fields = ["id", "creado"]
