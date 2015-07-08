# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0031_auto_20150708_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='group',
            field=models.ForeignKey(default=None, to='settings.ClientGroup'),
            preserve_default=False,
        ),
    ]
