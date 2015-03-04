# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0015_auto_20150301_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='group',
            field=models.OneToOneField(related_name='Group', null=True, default=None, blank=True, to='settings.Group'),
            preserve_default=True,
        ),
    ]
