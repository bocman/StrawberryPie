# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0006_auto_20160329_2229'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='group',
            table='Group',
        ),
    ]
