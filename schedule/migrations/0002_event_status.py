# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.PositiveIntegerField(default=101, choices=[(101, 'Not Confirmed'), (102, 'Confirmed'), (103, 'Delayed'), (104, 'Cancelled'), (105, 'Concluded')]),
            preserve_default=False,
        ),
    ]
