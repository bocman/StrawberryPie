# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0001_initial'),
    ]

    operations = [
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
                ('group', models.ForeignKey(default=None, to='setting.ClientGroup')),
            ],
            options={
                'db_table': 'modul',
            },
        ),
        migrations.RemoveField(
            model_name='item',
            name='client',
        ),
        migrations.RemoveField(
            model_name='item',
            name='group',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
