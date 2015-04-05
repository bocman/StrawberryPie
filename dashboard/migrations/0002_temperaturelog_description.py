# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperaturelog',
            name='description',
            field=models.CharField(default=b'-', max_length=30, verbose_name='Description'),
            preserve_default=True,
        ),
    ]
