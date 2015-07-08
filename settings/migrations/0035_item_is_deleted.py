# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0034_item_is_activated'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_deleted',
            field=models.BooleanField(default=False, help_text=b'Status which indicate if Item is assigned as deleted'),
        ),
    ]
