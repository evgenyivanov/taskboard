# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-10-08 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20171008_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='comments',
            field=models.CharField(max_length=200),
        ),
    ]
