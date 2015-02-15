# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0008_auto_20150208_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='status',
            field=models.BooleanField(default=False, help_text=b'If client is currently connected'),
            preserve_default=True,
        ),
    ]
