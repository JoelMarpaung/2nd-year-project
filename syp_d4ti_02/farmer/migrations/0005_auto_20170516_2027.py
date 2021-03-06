# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-16 13:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0004_auto_20170515_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='PengajuanLahan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_certificate', models.ImageField(blank=True, upload_to='pengajuanLahan')),
                ('luas_lahan', models.CharField(max_length=20, null=True)),
                ('alamat_lahan', models.TextField(null=True)),
                ('status', models.CharField(max_length=30, null=True)),
                ('keterangan', models.TextField(null=True)),
                ('tanggal_pengajuan', models.DateTimeField(max_length=20, null=True)),
                ('disetujui', models.CharField(max_length=10, null=True)),
                ('alasan_penolakan', models.TextField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='akun',
            name='jenis_akun',
            field=models.CharField(choices=[('farmer', 'Farmer'), ('admin', 'Admin'), ('surveyer', 'Surveyer'), ('quality', 'Quality')], max_length=10),
        ),
        migrations.AlterField(
            model_name='pengguna',
            name='full_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pengguna',
            name='kabupaten',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pengguna',
            name='kecamatan',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pengguna',
            name='photo',
            field=models.ImageField(blank=True, upload_to='users'),
        ),
        migrations.AlterField(
            model_name='pengguna',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pengajuanlahan',
            name='farmer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.Pengguna'),
        ),
    ]
