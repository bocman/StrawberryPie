# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0038_alarm_passed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alarm',
            old_name='passed',
            new_name='is_passed',
        ),
        migrations.AddField(
            model_name='alarm',
            name='is_periodically',
            field=models.BooleanField(default=False),
        ),
    ]
