# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('setting', '0004_auto_20151020_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEmailSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disable_email_notifications', models.BooleanField(default=False, help_text=b'Disable all email notifications.')),
                ('send_morning_report', models.BooleanField(default=False, help_text=b'Send me morning report.')),
                ('when_my_event_start', models.BooleanField(default=False, help_text=b'Notify me, when my event has started')),
                ('when_my_event_end', models.BooleanField(default=False, help_text=b'Notify me, when my event is done')),
                ('someone_cancel_my_event', models.BooleanField(default=False, help_text=b'Notify me, if someone has cancel my event')),
                ('client_become_unreachable', models.BooleanField(default=False, help_text=b'Notify me, when client become unreachable')),
                ('client_become_available', models.BooleanField(default=False, help_text=b'Notify me, when client become connected')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_email_settings',
            },
        ),
    ]
