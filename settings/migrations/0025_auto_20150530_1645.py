# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0024_auto_20150530_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='last_active',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
