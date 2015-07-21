# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0042_remove_alarm_notified'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarm',
            name='group',
            field=models.ForeignKey(default=None, to='settings.ClientGroup'),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_active',
            field=models.DateTimeField(),
        ),
    ]
