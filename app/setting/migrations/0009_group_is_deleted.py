# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0008_remove_group_clients_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='is_deleted',
            field=models.BooleanField(default=False, help_text=b'Status which indicate if group is marked as deleted'),
        ),
    ]
