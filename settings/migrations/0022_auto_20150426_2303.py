# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0021_alarm_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarm',
            name='notified',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alarm',
            name='alarm_volume',
            field=models.PositiveIntegerField(default=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alarm',
            name='client',
            field=models.ForeignKey(to='settings.Client'),
            preserve_default=True,
        ),
    ]
