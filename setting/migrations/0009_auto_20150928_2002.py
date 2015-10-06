# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0008_auto_20150828_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='task_id',
            new_name='end_task_id',
        ),
        migrations.AddField(
            model_name='event',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='start_task_id',
            field=models.CharField(max_length=36, null=True),
        ),
    ]
