# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_auto_20160221_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='disponible',
            field=models.BooleanField(default=False),
        ),
    ]
