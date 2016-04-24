# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0005_useremailsettings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ElementGroup',
            new_name='Group',
        ),
    ]
