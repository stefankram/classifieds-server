# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 01:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170209_0051'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(db_column='latitude')),
                ('longitude', models.FloatField(db_column='longitude')),
                ('seller_id', models.ForeignKey(db_column='seller_id', on_delete=django.db.models.deletion.CASCADE, to='api.SellerModel')),
            ],
        ),
    ]
