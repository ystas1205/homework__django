from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.name


class TemperatureMeasurement(models.Model):
    sensor = models.ForeignKey(
        Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(verbose_name='Температура')
    date_time_measurement = models.DateTimeField(auto_now_add=True,
                                                 verbose_name='Дата и время '
                                                 'измерения')
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)
