# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0012_remove_client_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='group',
            field=models.ForeignKey(related_name='Group', default=None, to='settings.Client'),
            preserve_default=True,
        ),
    ]
