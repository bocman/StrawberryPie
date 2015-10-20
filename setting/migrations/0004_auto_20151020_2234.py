# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0003_auto_20151020_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='is_connected',
        ),
        migrations.AlterField(
            model_name='client',
            name='last_active',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
