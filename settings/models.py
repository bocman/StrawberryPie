from django.db import models
from core.managers import ActiveClientsManager
from django.utils.translation import ugettext as _


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
    last_active = models.DateTimeField(default=None)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'client'

    objects = models.Manager()
    active = ActiveClientsManager()
