# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0019_alarm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarm',
            name='notification_time',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
