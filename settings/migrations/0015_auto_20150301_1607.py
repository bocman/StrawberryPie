# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0014_auto_20150301_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='group',
            field=models.ForeignKey(related_name='Group', default=None, blank=True, to='settings.Group', null=True),
            preserve_default=True,
        ),
    ]
