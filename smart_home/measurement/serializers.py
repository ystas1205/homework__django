from rest_framework import serializers
from measurement.models import TemperatureMeasurement, Sensor


class TemperatureMeasurementSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(allow_empty_file=True, use_url=False)

    class Meta:
        model = TemperatureMeasurement
        fields = ['sensor', 'temperature', 'date_time_measurement', 'photo']


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = TemperatureMeasurementSerializer(many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

# TODO: опишите необходимые сериализаторы
