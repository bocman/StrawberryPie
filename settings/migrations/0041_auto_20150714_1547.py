# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0040_auto_20150714_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarm',
            name='notification_time',
            field=models.CharField(help_text=b"Enter execution time in 'xx-xx-xx xx:xx' style", max_length=50),
        ),
    ]
