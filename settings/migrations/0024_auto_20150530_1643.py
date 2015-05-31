# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0023_client_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='key',
            field=models.CharField(default=None, max_length=32, unique=True, null=True, blank=True),
        ),
    ]
