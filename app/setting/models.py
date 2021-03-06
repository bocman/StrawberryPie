from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils import timezone as tz
from datetime import timedelta
from djcelery.models import TaskState


from celery.result import AsyncResult
import logging
import requests
import json
from requests.exceptions import ConnectionError

from dateutil.parser import parse
from datetime import date
from collections import defaultdict

from django.contrib.auth.models import User
from core.utils import codes, format_time_interval, format_datetime
from core.managers import ActiveClientsManager, OnlineClientsManager, ActiveModulsManager

log = logging.getLogger(__name__)




class Group(models.Model):

    """
    TODO
    """
    class Meta:
        db_table = 'Group'

    name = models.CharField(
        verbose_name=_('Group name'),
        max_length=20,
    )
    description = models.CharField(
        verbose_name=_('Short description'),
        max_length=30,
        help_text="Short summary of the group"
    )
    is_deleted = models.BooleanField(
        default=False,
        help_text="Status which indicate if group is marked as deleted"
    )

    def __str__(self):
        return self.name


class Client(models.Model):

    """
    This model represent Client
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
    group = models.ForeignKey(
        Group, 
        on_delete=models.CASCADE,
        default = None
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
    last_active = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
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

    def is_connected(self):
        """
        We use this function to check connection with client.
        It's like a simple ping method
        """
        url = "http://{0}/api/ping/".format(str(self.ip_address))
        try:
            r = requests.get(url, timeout=3.0)
            if r.status_code == requests.codes.ok:
                return True
            else:
                return False
        except ConnectionError: 
            return False
        except requests.exceptions.Timeout:
            return False

    def all_moduls(self):
        links ={
            'port': "http://{0}:{1}/api/gpio/all/",
            'no_port': "http://{0}/api/gpio/all/"
        }
        if not self.is_connected:
            return codes.error
        if self.port:
            url = links['port'].format(
                self.ip_address, self.port
                )
        else:
            url = links['no_port'].format(
                self.ip_address
                )
        try:
            r = requests.get(url, timeout=3.0)
            if r.status_code == requests.codes.ok:
                moduls = json.loads(r.text)
                for i in moduls:
                    group_id = i.get('group', None)
                    #i['group'] = ClientGroup.objects.get(id=group_id)
                return moduls
            else:
                return codes.error
        except requests.exceptions.Timeout:
            return codes.error
        except requests.exceptions.ConnectionError:
            return codes.error

    def moduls(self):
        all_moduls = self.all_moduls()
        if all_moduls is not codes.error:
            seznam = []
            for modul in all_moduls:
                if modul['is_used']:
                    seznam.append(modul)
            return seznam
        return None



class Modul(models.Model):
    """
    Class is used to hold information about specifiv modul. Modul can 
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
    group = models.ForeignKey(
        Group, 
        on_delete=models.CASCADE,
        default = None
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
        verbose_name=_('Event name'),
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

    def status(self):
        start = AsyncResult(self.start_task_id)
        end = AsyncResult(self.end_task_id)


    def clean(self):
        errors = defaultdict()
        if self.start_time > self.end_time:
            errors['start_time'] = _('Start time should be less then end time.')
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
        Group,
        null=True,
        blank=True
        )


class UserEmailSettings(models.Model):
    """
    This model hold all settings about sending email to users.
    Each user have unique email settings, which is related with foreign key.
    """
    class Meta:
        db_table = 'user_email_settings'

    user = models.ForeignKey(User)
    disable_email_notifications = models.BooleanField(
        default=False, null=False, blank=False,
        help_text="Disable all email notifications."
    )
    send_morning_report = models.BooleanField(
        default=False, null=False, blank=False,
        help_text="Send me morning report."
    )
    when_my_event_start = models.BooleanField(
        default=False, null=False, blank=False,
        help_text="Notify me, when my event has started"
    )
    when_my_event_end = models.BooleanField(
        default=False, null=False, blank=False,
        help_text="Notify me, when my event is done"
    )
    someone_cancel_my_event = models.BooleanField(
        default=False, null=False, blank=False,
        help_text="Notify me, if someone has cancel my event"
    )
    client_become_unreachable = models.BooleanField(
        default=False, null=False, blank=False,
        help_text="Notify me, when client become unreachable"
    )
    client_become_available = models.BooleanField(
        default=False, null=False, blank=False,
        help_text="Notify me, when client become connected"
    )