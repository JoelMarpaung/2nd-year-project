# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-17 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0007_auto_20170516_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data_pengajuan_lahan',
            name='disetujui',
        ),
        migrations.AlterField(
            model_name='data_pengajuan_lahan',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]