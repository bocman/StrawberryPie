# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20150405_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperaturelog',
            name='humidity',
            field=models.SmallIntegerField(default=None, null=True, verbose_name='Humidity'),
            preserve_default=True,
        ),
    ]
