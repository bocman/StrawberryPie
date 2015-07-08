# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0033_auto_20150708_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_activated',
            field=models.BooleanField(default=False),
        ),
    ]
