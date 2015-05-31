# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0017_auto_20150324_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='realibility',
            field=models.PositiveSmallIntegerField(default=0, help_text=b'Daily count of the client disconections', verbose_name='CLient realibility'),
            preserve_default=True,
        ),
    ]
