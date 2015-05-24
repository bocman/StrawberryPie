from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class TemperatureLog(models.Model):

    temp = models.SmallIntegerField(
        verbose_name=_('Temperature'),
        default=None, null=True
    )
    humidity = models.SmallIntegerField(
        verbose_name=_('Humidity'),
        default=None, null=True
    )
    wind = models.SmallIntegerField(
        verbose_name=_('Wind'),
        default=None, null=True
    )
    city = models.CharField(
        verbose_name=_('City'),
        max_length=30, null=False,
        default="-"
    )
    feels_like = models.SmallIntegerField(
        verbose_name=_('Feels like'),
        default=None, null=True
    )
    description = models.CharField(
        verbose_name=_('Description'),
        max_length=30, null=False, default="-"
    )
    timestamp = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'temperature_log'
