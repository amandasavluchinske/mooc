# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-11 18:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180410_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Data de entrada'),
            preserve_default=False,
        ),
    ]
