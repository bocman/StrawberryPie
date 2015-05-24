# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0016_auto_20150301_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='status',
        ),
        migrations.AddField(
            model_name='client',
            name='last_active',
            field=models.DateTimeField(default=None),
            preserve_default=True,
        ),
    ]
