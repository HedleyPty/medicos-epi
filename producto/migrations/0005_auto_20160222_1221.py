# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_auto_20160222_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
        migrations.AddField(
            model_name='producto',
            name='archivo_app',
            field=models.FileField(blank=True, null=True, upload_to=b'/home/hedley/Tienda/media/'),
        ),
    ]
