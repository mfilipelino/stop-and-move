# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 03:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_stopbus_poly'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='route',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Route'),
        ),
    ]
