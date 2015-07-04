# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0028_auto_20150621_1145'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Group',
            new_name='ClientGroup',
        ),
    ]
