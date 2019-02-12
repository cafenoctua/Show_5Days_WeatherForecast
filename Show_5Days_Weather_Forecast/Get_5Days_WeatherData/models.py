from django.db import models

# # Create your models here.

class InputCity(models.Model):

    input_city_name = models.CharField(
        max_length = 100,
        verbose_name='City:',
    )

    def __str__(self):
        return self.input_city_name
    
class WeatherData(models.Model):
    time = models.CharField(
        max_length=100,
    )
    weather = models.CharField(
        max_length=100,
    )
    temperature = models.FloatField(
    )
    rainfall = models.FloatField(
    )