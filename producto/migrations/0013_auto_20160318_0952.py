# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-18 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0012_auto_20160318_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='repos',
            field=models.CharField(blank=True, default=b'', max_length=200, null=True),
        ),
    ]