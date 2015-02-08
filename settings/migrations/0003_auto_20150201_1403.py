# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_auto_20150126_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='ip_adress',
        ),
        migrations.AddField(
            model_name='client',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 1, 14, 3, 22, 977483, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='deleted',
            field=models.BooleanField(default=False, help_text=b'Status which indicate if client is assigned as deleted'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='disabled',
            field=models.BooleanField(default=False, help_text=b'Status which indicate if client is assigned as disabled'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='ip_address',
            field=models.GenericIPAddressField(default=None, blank=True, help_text=b'IP address of the client', null=True, verbose_name='IP address'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='last_successfull_ip_address',
            field=models.GenericIPAddressField(default=None, blank=True, help_text=b'Last succesfull IP adress, which client use to authenticate', null=True, verbose_name='Last succesfull IP address'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='port',
            field=models.PositiveIntegerField(default=None, help_text=b'Port number which is used to make connection with client', null=True, verbose_name='Port number', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='description',
            field=models.CharField(help_text=b'Short summary of the client', max_length=30, verbose_name='Short description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(help_text=b'Client name which is connectinng to the server', max_length=15, verbose_name='Client name'),
            preserve_default=True,
        ),
    ]
