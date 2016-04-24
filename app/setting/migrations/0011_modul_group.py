# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0010_client_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='modul',
            name='group',
            field=models.ForeignKey(default=None, to='setting.Group'),
        ),
    ]
