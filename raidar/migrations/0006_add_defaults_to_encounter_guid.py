# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-12 02:01
from __future__ import unicode_literals

from django.db import migrations

def gen_guid(apps, schema_editor):
    Encounter = apps.get_model('raidar', 'Encounter')
    for row in Encounter.objects.all():
        row.guid = "old-%012x" % row.id
        row.save(update_fields=['guid'])

class Migration(migrations.Migration):

    dependencies = [
        ('raidar', '0005_encounter_guid'),
    ]

    operations = [
        migrations.RunPython(gen_guid, reverse_code=migrations.RunPython.noop),
    ]
