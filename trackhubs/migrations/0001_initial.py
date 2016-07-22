# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 11:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genomebrowser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('short_label', models.CharField(max_length=500)),
                ('long_label', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('short_label', models.CharField(max_length=500)),
                ('long_label', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=500)),
                ('track_type', models.CharField(max_length=500)),
                ('color', models.CharField(max_length=500)),
                ('Supertrack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackhubs.SuperTrack')),
            ],
        ),
        migrations.CreateModel(
            name='TrackHub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hub_name', models.CharField(max_length=500)),
                ('short_label', models.CharField(max_length=500)),
                ('long_label', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=500)),
                ('Genome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genomebrowser.Genome')),
            ],
        ),
        migrations.AddField(
            model_name='supertrack',
            name='TrackHub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackhubs.TrackHub'),
        ),
    ]