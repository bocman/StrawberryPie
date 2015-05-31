# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_auto_20150201_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='last_successfull_ip_address',
        ),
    ]
