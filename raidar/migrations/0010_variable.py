# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-19 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raidar', '0009_add_user_profiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('key', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('value', models.TextField(null=True)),
            ],
        ),
    ]