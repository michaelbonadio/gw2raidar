# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-13 07:35
from __future__ import unicode_literals

from django.db import migrations, models


def set_account_and_char_name(apps, schema_editor):
    Participation = apps.get_model('raidar', 'Participation')
    for participation in Participation.objects.all().select_related('character').iterator():
        participation.account_id = participation.character.account_id
        participation.character_name = participation.character.name
        participation.profession = participation.character.profession
        participation.save()


class Migration(migrations.Migration):

    dependencies = [
        ('raidar', '0033_add_account_to_participation'),
    ]

    operations = [
        migrations.RunPython(set_account_and_char_name, migrations.RunPython.noop)
    ]
