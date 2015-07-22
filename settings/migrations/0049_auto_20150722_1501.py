# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0048_auto_20150722_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarm',
            name='end_time',
            field=models.DateTimeField(help_text='Enter time, when this action should end'),
        ),
        migrations.AlterField(
            model_name='alarm',
            name='start_time',
            field=models.DateTimeField(help_text='Enter time, when this action should start'),
        ),
    ]
