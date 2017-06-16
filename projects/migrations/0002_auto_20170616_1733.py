# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-16 17:33
from __future__ import unicode_literals

from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=projects.models.upload_location),
        ),
    ]
