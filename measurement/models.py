from django.db import models
from django.utils import timezone


class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Measurement(models.Model):
    created_at = models.DateField(default=timezone.now)
    temperature = models.DecimalField(decimal_places=1, max_digits=3)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

