# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0043_auto_20150715_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarm',
            name='group',
            field=models.ForeignKey(to='settings.ClientGroup'),
        ),
    ]
