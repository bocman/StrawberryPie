# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_auto_20150201_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='port',
            field=models.PositiveSmallIntegerField(default=None, help_text=b'Port number which is used to make connection with client', null=True, verbose_name='Port number', blank=True),
            preserve_default=True,
        ),
    ]
