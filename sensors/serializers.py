# sensor_app/serializers.py
from rest_framework import serializers
from .models import SensorData

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['temperature', 'humidity', 'wind_speed']
