# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0049_auto_20150722_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarm',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='alarm',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
