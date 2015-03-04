# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0013_client_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='group',
            field=models.ForeignKey(related_name='Group', default=None, blank=True, to='settings.Client', null=True),
            preserve_default=True,
        ),
    ]
