# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0026_auto_20150530_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_type',
            field=models.CharField(default=b'Normal', max_length=20, choices=[(b'Normal', b'Normal'), (b'RPi', b'Raspberry Pi')]),
        ),
    ]
