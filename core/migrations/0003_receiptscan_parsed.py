# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170210_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiptscan',
            name='parsed',
            field=models.TextField(default=''),
        ),
    ]
