# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0011_auto_20150301_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='group',
        ),
    ]
