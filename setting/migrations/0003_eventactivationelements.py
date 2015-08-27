# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0002_auto_20150826_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventActivationElements',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event', models.ForeignKey(to='setting.Event')),
                ('modul', models.ForeignKey(to='setting.Modul')),
            ],
            options={
                'db_table': 'event_activations',
            },
        ),
    ]
