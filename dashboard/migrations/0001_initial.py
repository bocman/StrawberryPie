# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TemperatureLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temp', models.SmallIntegerField(default=None, null=True, verbose_name='Temperature')),
                ('humidity', models.SmallIntegerField(default=None, null=True, verbose_name='Humidity')),
                ('wind', models.SmallIntegerField(default=None, null=True, verbose_name='Wind')),
                ('city', models.CharField(default=b'-', max_length=30, verbose_name='City')),
                ('feels_like', models.SmallIntegerField(default=None, null=True, verbose_name='Feels like')),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'temperature_log',
            },
            bases=(models.Model,),
        ),
    ]
