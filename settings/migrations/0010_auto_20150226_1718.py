# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0009_client_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='status',
            field=models.BooleanField(default=False, help_text=b'Is client is currently connected'),
            preserve_default=True,
        ),
    ]
