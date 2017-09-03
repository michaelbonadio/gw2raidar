# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-12 02:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raidar', '0006_add_first_era'),
    ]

    operations = [
        migrations.AddField(
            model_name='encounter',
            name='era',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='encounters', to='raidar.Era'),
            preserve_default=False,
        ),
    ]
