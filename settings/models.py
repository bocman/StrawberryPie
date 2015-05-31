from django.db import models
from core.managers import ActiveClientsManager, OnlineClientsManager
from django.utils.translation import ugettext as _
from django.utils import timezone as tz

class Group(models.Model):

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
    group = models.OneToOneField(
        "Group", default=None, null=True, blank=True, related_name='Group')

    deleted = models.BooleanField(
        default=False,
        help_text="Status which indicate if client is assigned as deleted"
    )
    disabled = models.BooleanField(
        default=False,
        help_text="Status which indicate if client is assigned as disabled"
    )
    last_active = models.DateTimeField(auto_now=True)
    
    created = models.DateTimeField(auto_now=True)

    realibility = models.PositiveSmallIntegerField(
        verbose_name=_('CLient realibility'), default=0,
        help_text="Daily count of the client disconections"
    )
    client_key =  models.CharField(
        unique=True, max_length=32,
        null=True, blank=True,
        default=None
        )

    def is_active(self):
        now = tz.now()
        return True if self.last_active and (now - self.last_active).seconds < 60 else False 

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
        help_text='Short notes about this alarm'
        )

    alarm_volume = models.PositiveIntegerField(
        default=100        )
    
    notification_time = models.CharField(
        max_length=50
        )

    notified = models.BooleanField(
        default=False,
        blank=False, null=False
        )

    client = models.ForeignKey(
        "Client",
        blank=False, null=False
        )




