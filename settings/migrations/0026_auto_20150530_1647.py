# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0025_auto_20150530_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='key',
            new_name='client_key',
        ),
    ]
