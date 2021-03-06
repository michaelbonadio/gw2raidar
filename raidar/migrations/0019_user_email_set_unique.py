# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-04 02:15
from __future__ import unicode_literals

from django.db import migrations, models
from types import MethodType


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('raidar', '0018_path_of_fire'),
    ]

    op = migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address'),
        )


    # XXX HACK warning
    def state_forwards(self, app_label, state):
        self.state_forwards_backup('auth', state)
    op.state_forwards_backup = op.state_forwards
    op.state_forwards = MethodType(state_forwards, op)
    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        self.database_forwards_backup('auth', schema_editor, from_state, to_state)
    op.database_forwards_backup = op.database_forwards
    op.database_forwards = MethodType(database_forwards, op)


    operations = [
        op
    ]
