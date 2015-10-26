# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Client name which is connectinng to the server', max_length=20, verbose_name='Client name')),
                ('description', models.CharField(help_text=b'Short summary of the client', max_length=30, verbose_name='Short description')),
                ('ip_address', models.GenericIPAddressField(null=True, default=None, blank=True, help_text=b'IP address of the client', unique=True, verbose_name='IP address')),
                ('port', models.PositiveSmallIntegerField(default=None, help_text=b'Port number which is used to make connection with client', null=True, verbose_name='Port number', blank=True)),
                ('deleted', models.BooleanField(default=False, help_text=b'Status which indicate if client is assigned as deleted')),
                ('disabled', models.BooleanField(default=False, help_text=b'Status which indicate if client is assigned as disabled')),
                ('last_active', models.DateTimeField(default=None, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('realibility', models.PositiveSmallIntegerField(default=0, help_text=b'Daily count of the client disconections', verbose_name='CLient realibility')),
                ('key', models.CharField(default=None, max_length=32, unique=True, null=True, blank=True)),
                ('type', models.CharField(default=b'Normal', max_length=20, choices=[(b'Normal', b'Normal'), (b'RPi', b'Raspberry Pi')])),
            ],
            options={
                'db_table': 'client',
            },
        ),
        migrations.CreateModel(
            name='ElementGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Group name')),
                ('description', models.CharField(help_text=b'Short summary of the group', max_length=30, verbose_name='Short description')),
                ('clients_number', models.PositiveSmallIntegerField(default=0, help_text=b'Number of clients in the group', verbose_name='Number of clients')),
            ],
            options={
                'db_table': 'client_group',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, help_text='Name tag of the event', max_length=30, verbose_name=b'Event name')),
                ('note', models.CharField(help_text='Short notes about this event', max_length=50, verbose_name=b'Notes')),
                ('start_task_id', models.CharField(max_length=36, null=True)),
                ('end_task_id', models.CharField(max_length=36, null=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('is_passed', models.BooleanField(default=False)),
                ('is_periodically', models.BooleanField(default=False, verbose_name='Repet periodically')),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='EventActivationElements',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event', models.ForeignKey(to='setting.Event')),
                ('group', models.ForeignKey(blank=True, to='setting.ElementGroup', null=True)),
            ],
            options={
                'db_table': 'event_activations',
            },
        ),
        migrations.CreateModel(
            name='Modul',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='Name of the modul')),
                ('description', models.CharField(help_text=b'Short summary of the modul', max_length=30, verbose_name='Short description')),
                ('is_general', models.BooleanField(default=False)),
                ('pin_number', models.PositiveIntegerField(default=None, null=True)),
                ('interval', models.PositiveIntegerField(default=0, help_text=b'Time interval- need to complete', null=True, verbose_name=b'Time interval')),
                ('is_input', models.NullBooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False, help_text=b'Status which indicate if modul is assigned as deleted')),
                ('is_activated', models.BooleanField(default=False, help_text=b'Status which indicate if modul is activated')),
                ('client', models.ForeignKey(default=None, blank=True, to='setting.Client', null=True)),
            ],
            options={
                'db_table': 'modul',
            },
        ),
        migrations.AddField(
            model_name='eventactivationelements',
            name='modul',
            field=models.ForeignKey(blank=True, to='setting.Modul', null=True),
        ),
    ]
