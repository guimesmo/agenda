# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 01:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20150607_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('method', models.PositiveIntegerField(choices=[(100, 'Dinheiro'), (101, 'Cartão de débito'), (102, 'Cartão de crédito'), (103, 'Cheque')])),
                ('additional_comments', models.CharField(max_length=100)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Event')),
            ],
        ),
    ]
