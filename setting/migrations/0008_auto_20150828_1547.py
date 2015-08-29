# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0007_auto_20150828_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(default=None, help_text='Name tag of the event', max_length=30, verbose_name=b'Event name'),
        ),
    ]
