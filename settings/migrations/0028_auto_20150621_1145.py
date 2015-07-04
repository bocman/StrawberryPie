# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0027_client_client_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='client_key',
            new_name='key',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_type',
            new_name='type',
        ),
    ]
