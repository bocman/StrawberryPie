# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0011_auto_20151008_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='last_active',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
