# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0039_auto_20150714_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarm',
            name='is_periodically',
            field=models.BooleanField(default=False, verbose_name=b'Repet periodically'),
        ),
    ]
