# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 00:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyermodel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='buyermodel',
            name='email',
        ),
        migrations.RemoveField(
            model_name='buyermodel',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='buyermodel',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='buyermodel',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='companymodel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='companymodel',
            name='email',
        ),
        migrations.RemoveField(
            model_name='companymodel',
            name='name',
        ),
        migrations.RemoveField(
            model_name='companymodel',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='sellermodel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='sellermodel',
            name='email',
        ),
        migrations.RemoveField(
            model_name='sellermodel',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='sellermodel',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='sellermodel',
            name='updated_at',
        ),
    ]
