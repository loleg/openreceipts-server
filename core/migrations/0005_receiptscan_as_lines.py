# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170210_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiptscan',
            name='as_lines',
            field=models.TextField(default=''),
        ),
    ]
