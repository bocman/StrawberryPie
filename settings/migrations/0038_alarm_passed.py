# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0037_auto_20150708_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarm',
            name='passed',
            field=models.BooleanField(default=False),
        ),
    ]
