# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schedule', '0002_event_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='creation_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 7, 19, 54, 33, 199344, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='creation_user',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='last_edition',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 7, 19, 54, 58, 555732, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='comment',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.PositiveIntegerField(default=101, choices=[(101, 'Not Confirmed'), (102, 'Confirmed'), (103, 'Delayed'), (104, 'Cancelled'), (105, 'Concluded')]),
        ),
    ]
