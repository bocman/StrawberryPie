# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=30)),
                ('ip_adress', models.GenericIPAddressField(default=None, null=True, verbose_name='Ip address', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
