# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-29 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookBuyer', '0003_auto_20160829_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='cost',
            name='user',
            field=models.CharField(default='Null', max_length=20),
            preserve_default=False,
        ),
    ]
