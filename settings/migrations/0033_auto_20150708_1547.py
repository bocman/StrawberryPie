# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0032_client_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='notified',
            new_name='is_general',
        ),
        migrations.AddField(
            model_name='item',
            name='client',
            field=models.ForeignKey(default=None, blank=True, to='settings.Client', null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='group',
            field=models.ForeignKey(default=None, to='settings.ClientGroup'),
        ),
        migrations.AddField(
            model_name='item',
            name='is_input',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='pin_number',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
    ]
