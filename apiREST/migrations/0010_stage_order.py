# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiREST', '0009_auto_20171123_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]