# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0022_auto_20150426_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='key',
            field=models.CharField(default=None, max_length=40, unique=True, null=True, blank=True),
        ),
    ]
