# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20170227_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagemodel',
            name='message',
            field=models.TextField(db_column='message'),
        ),
    ]
