from django.db import models
from managers import ActiveClientsManager
from django.utils.translation import ugettext as _


class Client(models.Model):
    """
    This model is used to store Clients, which are in use to connect to
    Strawberry Pie
    """

    name = models.CharField(
        verbose_name=_('Client name'),
        max_length=15,
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
    created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'client'

    objects = models.Manager()
    active = ActiveClientsManager()













