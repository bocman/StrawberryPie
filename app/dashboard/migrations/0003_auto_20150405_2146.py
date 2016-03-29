# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_temperaturelog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperaturelog',
            name='humidity',
            field=models.CharField(default=None, max_length=30, null=True, verbose_name='Humidity'),
            preserve_default=True,
        ),
    ]
