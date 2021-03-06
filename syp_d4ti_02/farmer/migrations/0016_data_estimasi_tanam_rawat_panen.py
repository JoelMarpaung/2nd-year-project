# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-23 09:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0015_auto_20170523_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data_Estimasi_Tanam_Rawat_Panen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_estimasi', models.CharField(blank=True, max_length=50)),
                ('keterangan', models.TextField(blank=True)),
                ('tanggal_estimasi', models.DateField(blank=True)),
                ('lahan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.Data_Lahan')),
            ],
        ),
    ]
