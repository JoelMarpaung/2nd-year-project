# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-15 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0003_pengguna_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pengguna',
            name='email',
        ),
        migrations.RemoveField(
            model_name='pengguna',
            name='provinsi',
        ),
        migrations.AlterField(
            model_name='pengguna',
            name='alamat',
            field=models.TextField(null=True),
        ),
    ]