# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 02:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0003_subscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribe',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
