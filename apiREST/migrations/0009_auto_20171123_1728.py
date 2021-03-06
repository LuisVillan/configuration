# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-23 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiREST', '0008_auto_20171101_0354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('scenario', models.IntegerField(default=0)),
                ('position', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='description',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='presentation',
            field=models.CharField(default='', max_length=70),
            preserve_default=False,
        ),
    ]
