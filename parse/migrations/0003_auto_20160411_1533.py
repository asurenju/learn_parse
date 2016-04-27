# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 07:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('parse', '0002_auto_20160411_1454'),
    ]

    operations = [
        migrations.DeleteModel(
            name='article_list',
        ),
        migrations.AddField(
            model_name='article',
            name='abstract',
            field=models.CharField(default=datetime.datetime(2016, 4, 11, 7, 33, 8, 283403, tzinfo=utc), max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]