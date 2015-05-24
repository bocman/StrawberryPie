# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0007_auto_20150208_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='ip_address',
            field=models.GenericIPAddressField(null=True, default=None, blank=True, help_text=b'IP address of the client', unique=True, verbose_name='IP address'),
            preserve_default=True,
        ),
    ]
