# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0029_auto_20150704_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='group',
            field=models.OneToOneField(related_name='ClientGroup', null=True, default=None, blank=True, to='settings.ClientGroup'),
        ),
    ]
