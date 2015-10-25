# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0002_client_is_connected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='last_active',
            field=models.DateTimeField(default=None),
        ),
    ]
