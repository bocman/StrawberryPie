# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0003_eventactivationelements'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Group name')),
                ('description', models.CharField(help_text=b'Short summary of the group', max_length=30, verbose_name='Short description')),
                ('clients_number', models.PositiveSmallIntegerField(default=0, help_text=b'Number of clients in the group', verbose_name='Number of clients')),
            ],
            options={
                'db_table': 'element_group',
            },
        ),
        migrations.RemoveField(
            model_name='modul',
            name='group',
        ),
        migrations.AlterField(
            model_name='eventactivationelements',
            name='modul',
            field=models.ForeignKey(blank=True, to='setting.Modul', null=True),
        ),
        migrations.DeleteModel(
            name='ClientGroup',
        ),
        migrations.AddField(
            model_name='eventactivationelements',
            name='group',
            field=models.ForeignKey(blank=True, to='setting.ElementGroup', null=True),
        ),
    ]
