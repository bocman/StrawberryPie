# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0035_item_is_deleted'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='item',
            table='items',
        ),
    ]
