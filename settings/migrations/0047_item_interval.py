# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0046_auto_20150721_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='interval',
            field=models.PositiveIntegerField(default=0, help_text=b'Time interval- need to complete', null=True, verbose_name=b'Time interval'),
        ),
    ]
