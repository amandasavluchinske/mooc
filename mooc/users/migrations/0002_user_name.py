# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-09 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
