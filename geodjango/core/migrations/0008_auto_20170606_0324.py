# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 03:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_track'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Track',
            new_name='Trajectory',
        ),
    ]
