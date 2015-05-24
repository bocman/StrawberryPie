# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_auto_20150202_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='ip_address',
            field=models.GenericIPAddressField(default=None, blank=True, help_text=b'IP address of the client', null=True, verbose_name='IP address'),
            preserve_default=True,
        ),
    ]
