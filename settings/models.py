from django.db import models
from core.managers import ActiveClientsManager, OnlineClientsManager, ActiveItemsManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone as tz
import logging

log = logging.getLogger(__name__)


class ClientGroup(models.Model):

    """
    TODO
    """
    name = models.CharField(
        verbose_name=_('Client group name'),
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
    group = models.ForeignKey(ClientGroup)

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


class Item(models.Model):
    """
    Class is used to hold information about some specific item. Item can 
    be related with client or not (Example: Webservice, which get data from web).
    Item can be defined as object, which get info(Service, sensors on GPIO ...) or
    can show result on the output.
    """
    class Meta:
        db_table = 'items'

    objects = models.Manager()
    active = ActiveItemsManager()

    name = models.CharField(
        verbose_name=_('Name of the item'),
        max_length=30,
    )
    description = models.CharField(
        verbose_name=_('Short description'),
        max_length=30,
        help_text="Short summary of the item"
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
    group = models.ForeignKey(ClientGroup, default=None)
    is_activated = models.BooleanField(
        default=False,
        blank=False, null=False
        )
    is_deleted = models.BooleanField(
        default=False,
        help_text="Status which indicate if Item is assigned as deleted"
    )
    is_activated = models.BooleanField(
        default=False,
        null=False, blank=False,
        help_text="Status which indicate if Item is activated"
    )

class Alarm(models.Model):
    """
    This model is used to represent alarm, which notify user about something.
    It can be used like a event reminder, timer ...
    """

    class Meta:
        db_table = 'alarm'

    note = models.CharField(
        max_length=50,
        verbose_name='Notes',
        help_text=_('Short notes about this alarm')
        )

    alarm_volume = models.PositiveIntegerField(
        default=100
        )
    start_time = models.DateTimeField(
        )
    end_time = models.DateTimeField(
        )
    client = models.ForeignKey(
        "Client",
        blank=False, null=False
        )
    group = models.ForeignKey(ClientGroup)
    is_passed = models.BooleanField(
        default=False,
        blank=False, null=False
        )
    is_periodically = models.BooleanField(
        default=False,
        blank=False, null=False,
        verbose_name=_('Repet periodically')
        )
    
    def execution_time(self):
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        else:
            return "N/A"

    def __str__(self):
        pass
        return self.client.name + str(self.start_time)
