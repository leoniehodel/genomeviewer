# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 07:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trackhubs', '0002_auto_20160720_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='TrackHub',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='trackhubs.TrackHub'),
        ),
    ]
