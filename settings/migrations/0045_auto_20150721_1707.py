# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0044_auto_20150715_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='is_activated',
            field=models.BooleanField(default=False, help_text=b'Status which indicate if Item is activated'),
        ),
    ]
