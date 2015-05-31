# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0020_auto_20150426_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarm',
            name='client',
            field=models.ForeignKey(default=None, to='settings.Client'),
            preserve_default=True,
        ),
    ]
