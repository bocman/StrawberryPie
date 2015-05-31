# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0018_client_realibility'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.CharField(help_text=b'Short notes about this alarm', max_length=50, verbose_name=b'Notes')),
                ('alarm_volume', models.IntegerField()),
                ('notification_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'alarm',
            },
            bases=(models.Model,),
        ),
    ]
