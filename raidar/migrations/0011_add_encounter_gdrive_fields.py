# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-12 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raidar', '0010_encounter_era'),
    ]

    operations = [
        migrations.AddField(
            model_name='encounter',
            name='gdrive_id',
            field=models.CharField(editable=False, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='encounter',
            name='gdrive_url',
            field=models.CharField(editable=False, max_length=255, null=True),
        ),
    ]
