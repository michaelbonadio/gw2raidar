# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-27 01:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('raidar', '0012_notification'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='upload',
            unique_together=set([('filename', 'uploaded_by')]),
        ),
    ]
