# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selfiecontest', '0021_auto_20170807_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picto',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
