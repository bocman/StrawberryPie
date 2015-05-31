# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0010_auto_20150226_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Client group name')),
                ('description', models.CharField(help_text=b'Short summary of the group', max_length=30, verbose_name='Short description')),
                ('clients_number', models.PositiveSmallIntegerField(default=0, help_text=b'Number of clients in the group', verbose_name='Number of clients')),
            ],
            options={
                'db_table': 'client_group',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='client',
            name='group',
            field=models.ForeignKey(default=None, to='settings.Group'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(help_text=b'Client name which is connectinng to the server', max_length=20, verbose_name='Client name'),
            preserve_default=True,
        ),
    ]
