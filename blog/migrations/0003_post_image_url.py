# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-03 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170222_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
