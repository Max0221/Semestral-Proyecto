from rest_framework import serializer
from core.models import Arte

class ObraSerializer(serializer.ModelSerializer):
    class Meta:
        model: Arte
        fields = '__all__'