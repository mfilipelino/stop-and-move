# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-03 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170603_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stop',
            name='latitude',
            field=models.DecimalField(decimal_places=51, max_digits=60),
        ),
        migrations.AlterField(
            model_name='stop',
            name='longitude',
            field=models.DecimalField(decimal_places=51, max_digits=60),
        ),
    ]
