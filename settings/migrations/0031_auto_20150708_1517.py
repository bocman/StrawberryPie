# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0030_auto_20150704_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Client group name')),
                ('description', models.CharField(help_text=b'Short summary of the group', max_length=30, verbose_name='Short description')),
                ('notified', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='client',
            name='group',
        ),
    ]
