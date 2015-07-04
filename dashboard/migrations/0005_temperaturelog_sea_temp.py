# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20150405_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperaturelog',
            name='sea_temp',
            field=models.SmallIntegerField(default=None, null=True, verbose_name='Sea temperature'),
        ),
    ]
