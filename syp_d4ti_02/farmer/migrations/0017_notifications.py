# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-11 13:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0016_data_estimasi_tanam_rawat_panen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pengirim', models.CharField(blank=True, max_length=50)),
                ('judul', models.CharField(blank=True, max_length=50)),
                ('keterangan', models.TextField(blank=True)),
                ('tanggal', models.DateField(blank=True)),
                ('status', models.TextField(max_length=50)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.Pengguna')),
            ],
        ),
    ]
