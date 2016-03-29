# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0007_auto_20160329_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='clients_number',
        ),
    ]
