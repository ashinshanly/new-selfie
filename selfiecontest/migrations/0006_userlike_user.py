# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selfiecontest', '0005_auto_20170724_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlike',
            name='user',
            field=models.CharField(default=3, max_length=250),
            preserve_default=False,
        ),
    ]