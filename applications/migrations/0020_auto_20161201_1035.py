# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-01 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0019_auto_20160628_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='rsvp_no_code',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='rsvp_yes_code',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
    ]
