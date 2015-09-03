from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils import timezone as tz
from datetime import timedelta
from djcelery.models import TaskState

from dateutil.parser import parse
import logging
from collections import defaultdict

from core.managers import ActiveClientsManager, OnlineClientsManager, ActiveModulsManager
from core.utils import format_time_interval, format_datetime

log = logging.getLogger(__name__)


class ElementGroup(models.Model):

    """
    TODO
    """
    class Meta:
        db_table = 'element_group'

    name = models.CharField(
        verbose_name=_('Group name'),
        max_length=20,
    )
    description = models.CharField(
        verbose_name=_('Short description'),
        max_length=30,
        help_text="Short summary of the group"
    )
    clients_number = models.PositiveSmallIntegerField(
        verbose_name=_('Number of clients'),
        default=0,
        help_text="Number of clients in the group"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'client_group'


class Client(models.Model):

    """
    This model is used to store Clients, which are in use to connect to
    Strawberry Pie
    """

    class Meta:
        db_table = 'client'

    objects = models.Manager()
    active = ActiveClientsManager()
    online = OnlineClientsManager()

    name = models.CharField(
        verbose_name=_('Client name'),
        max_length=20,
        help_text="Client name which is connectinng to the server"
    )
    description = models.CharField(
        verbose_name=_('Short description'),
        max_length=30,
        help_text="Short summary of the client"
    )
    ip_address = models.GenericIPAddressField(
        verbose_name=_('IP address'), blank=True,
        null=True, unique=True, default=None,
        help_text="IP address of the client"
    )
    port = models.PositiveSmallIntegerField(
        verbose_name=_('Port number'), blank=True,
        null=True, unique=False, default=None,
        help_text="Port number which is used to make connection with client"
    )

    deleted = models.BooleanField(
        default=False,
        help_text="Status which indicate if client is assigned as deleted"
    )
    disabled = models.BooleanField(
        default=False,
        help_text="Status which indicate if client is assigned as disabled"
    )
    last_active = models.DateTimeField()
    created = models.DateTimeField(auto_now=True)
    realibility = models.PositiveSmallIntegerField(
        verbose_name=_('CLient realibility'), default=0,
        help_text="Daily count of the client disconections"
    )
    key = models.CharField(
        unique=True, max_length=32,
        null=True, blank=True,
        default=None
        )
    CLIENT_TYPES = (
        ('Normal', 'Normal'),
        ('RPi', 'Raspberry Pi'),
    )
    type = models.CharField(
        max_length=20,
        choices=CLIENT_TYPES,
        default=CLIENT_TYPES[0][0]
        )

    def __str__(self):
        return self.name

    def is_active(self):
        now = tz.localtime(tz.now())
        last_active = tz.localtime(self.last_active)
        return True if last_active and (now - last_active).seconds < 60 else False



class Modul(models.Model):
    """
    Class is used to hold information about some specific modul. modul can 
    be related with client or not (Example: Webservice, which get data from web).
    modul can be defined as object, which get info(Service, sensors on GPIO ...) or
    can show result on the output.
    """
    class Meta:
        db_table = 'modul'

    objects = models.Manager()
    active = ActiveModulsManager()

    name = models.CharField(
        verbose_name=_('Name of the modul'),
        max_length=30,
    )
    description = models.CharField(
        verbose_name=_('Short description'),
        max_length=30,
        help_text="Short summary of the modul"
    )
    is_general = models.BooleanField(
        default=False,
        blank=False, null=False
        )
    pin_number = models.PositiveIntegerField(
        default=None, null=True
        )
    interval = models.PositiveIntegerField(
        default=0, null=True,
        blank=False,
        verbose_name="Time interval",
        help_text="Time interval- need to complete"
        )
    is_input = models.NullBooleanField(
        default=False,
        blank=True, null=True
        )
    client = models.ForeignKey(
        Client, default=None,
        blank=True, null=True
        )
    is_deleted = models.BooleanField(
        default=False,
        help_text="Status which indicate if modul is assigned as deleted"
    )
    is_activated = models.BooleanField(
        default=False,
        null=False, blank=False,
        help_text="Status which indicate if modul is activated"
    )


class Event(models.Model):
    """
    This model is used to represent Event
    """

    class Meta:
        db_table = 'event'

    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        default=None,
        verbose_name='Event name',
        help_text=_('Name tag of the event')
        )
    note = models.CharField(
        max_length=50,
        verbose_name='Notes',
        help_text=_('Short notes about this event')
        )
    start_task_id = models.CharField(
        max_length=36,
        null=True
        )
    end_task_id = models.CharField(
        max_length=36,
        null=True
        )   
    start_time = models.DateTimeField(
        )
    end_time = models.DateTimeField(
        )
    is_passed = models.BooleanField(
        default=False,
        blank=False, null=False
        )
    is_periodically = models.BooleanField(
        default=False,
        blank=False, null=False,
        verbose_name=_('Repet periodically')
        )
    is_active = models.BooleanField(
        default=False,
        blank=False, null=False
        )

    def execution_time(self):
        return format_time_interval(self.start_time, self.end_time)

    def get_start_time(self):
        return format_datetime(self.start_time)

    def get_end_time(self):
        return format_datetime(self.end_time)

    def is_activated(self):
        return True if self.is_active else False

    def clean(self):
        errors = defaultdict()
        if self.start_time > self.end_time:
            errors['start_time'] = _('Start time should be lesser then end time.')
        if self.end_time < self.start_time: 
            errors['end_time'] = _('End time should be greater then start time.')       
        
        raise ValidationError(errors)       



class EventActivationElements(models.Model):
    """
    Class is used to store relationships between event and
    Moduls/groups which will cooperate in activaton
    """
    class Meta:
        db_table = 'event_activations'

    event = models.ForeignKey(
        Event,
        null=False,
        blank=False
        )
    modul = models.ForeignKey(
        Modul,
        null=True,
        blank=True
        )
    group = models.ForeignKey(
        ElementGroup,
        null=True,
        blank=True
        )








