from rest_framework import serializers
from .models import temperature

class temperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = temperature
        fields = ('id', 'type', 'value')