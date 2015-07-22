# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0047_item_interval'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alarm',
            name='notification_time',
        ),
        migrations.AddField(
            model_name='alarm',
            name='end_time',
            field=models.CharField(default=None, help_text='Enter time, when this action should end', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alarm',
            name='start_time',
            field=models.CharField(default=None, help_text='Enter time, when this action should start', max_length=50),
            preserve_default=False,
        ),
    ]
