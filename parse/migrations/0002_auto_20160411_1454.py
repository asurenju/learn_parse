# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='link',
            field=models.CharField(max_length=400),
        ),
    ]
