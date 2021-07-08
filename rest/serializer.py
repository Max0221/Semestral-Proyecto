from rest_framework import serializer
from core.models import Obra

class ObraSerializer(serializer.ModelSerializer):
    class Meta:
        model: Obra
        fields = '__all__'