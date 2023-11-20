
from rest_framework import generics
from .models import Sensor, TemperatureMeasurement
from .serializers import SensorDetailSerializer, SensorSerializer, TemperatureMeasurementSerializer


# Чтение и создание датчика
class ReadingCreateAPIView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# Чтение и изменение датчика по id
class ReadingChangeAPIView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# Добавление измерения
class CreateAPIView(generics.CreateAPIView):
    queryset = TemperatureMeasurement.objects.all()
    serializer_class = TemperatureMeasurementSerializer

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
