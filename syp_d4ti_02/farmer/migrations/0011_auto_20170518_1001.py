# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-18 03:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0010_data_pengajuan_peminjaman_no_rekening'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data_Bibit_Pupuk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_komponen', models.CharField(max_length=50, null=True)),
                ('jenis_komponen', models.CharField(max_length=50, null=True)),
                ('keterangan', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Data_Gambar_Lahan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='dataLahan/gambar')),
            ],
        ),
        migrations.CreateModel(
            name='Data_Kegiatan_Pengolahan_Lahan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kegiatan', models.CharField(max_length=50, null=True)),
                ('keterangan', models.TextField(null=True)),
                ('tanggal_kegiatan', models.DateTimeField(null=True)),
                ('status', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Data_Komposisi_Lahan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_komposisi', models.CharField(max_length=50, null=True)),
                ('jenis_komposisi', models.CharField(max_length=50, null=True)),
                ('keterangan', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Data_Lahan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_certificate', models.ImageField(blank=True, upload_to='dataLahan/certificate')),
                ('luas_lahan', models.CharField(max_length=20, null=True)),
                ('alamat_lahan', models.TextField(null=True)),
                ('keterangan', models.TextField(null=True)),
                ('tanggal_pengajuan', models.DateTimeField(null=True)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.Pengguna')),
            ],
        ),
        migrations.CreateModel(
            name='Data_Peminjaman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=20, null=True)),
                ('no_rekening', models.CharField(max_length=30, null=True)),
                ('besar_peminjaman', models.CharField(max_length=20, null=True)),
                ('alasan_peminjaman', models.TextField(null=True)),
                ('tanggal_peminjaman', models.DateTimeField(null=True)),
                ('status', models.CharField(max_length=20, null=True)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.Pengguna')),
            ],
        ),
        migrations.AddField(
            model_name='data_komposisi_lahan',
            name='lahan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.Data_Lahan'),
        ),
        migrations.AddField(
            model_name='data_kegiatan_pengolahan_lahan',
            name='lahan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.Data_Lahan'),
        ),
        migrations.AddField(
            model_name='data_gambar_lahan',
            name='lahan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.Data_Lahan'),
        ),
        migrations.AddField(
            model_name='data_bibit_pupuk',
            name='lahan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.Data_Lahan'),
        ),
    ]
