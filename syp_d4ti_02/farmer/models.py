from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pengguna (models.Model):
	username = models.CharField(max_length=100, blank=True)
	full_name = models.CharField(max_length=100, blank=True)
	phone = models.CharField(max_length=30, blank=True)
	kabupaten = models.CharField(max_length=50, blank=True)
	kecamatan = models.CharField(max_length=50, blank=True)
	alamat = models.TextField(blank=True)
	photo = models.ImageField(upload_to='users', blank=True)

	def __str__(self):
		return self.full_name

class Akun (models.Model):
	JENIS_AKUN_CHOICES = (
		('farmer', 'Farmer'),
		('admin', 'Admin'),
		('surveyer', 'Surveyer'),
		('quality', 'Quality'),
	)
	akun = models.ForeignKey(User)	
	pengguna = models.ForeignKey(Pengguna)
	jenis_akun = models.CharField(max_length=10, choices=JENIS_AKUN_CHOICES)
	
	def __str__(self):
		return self.pengguna.full_name

class Data_Pengajuan_Lahan (models.Model):
	image_certificate = models.ImageField(upload_to='pengajuanLahan/certificate', blank=True)
	farmer = models.ForeignKey(Pengguna)
	luas_lahan = models.CharField(max_length=20, blank=True)
	alamat_lahan = models.TextField(blank=True)
	keterangan = models.TextField(blank=True)
	tanggal_pengajuan = models.DateTimeField(blank=True)
	status = models.CharField(max_length=20, blank=True)
	alasan_penolakan = models.TextField(blank=True)

	def __str__(self):
		return self.farmer.full_name

class Pengajuan_Gambar_Lahan (models.Model):
	image = models.ImageField(upload_to='pengajuanLahan/gambar', blank=True)
	gambar = models.CharField(max_length=20, blank=True)
	lahan = models.ForeignKey(Data_Pengajuan_Lahan)

	def __str__(self):
		return self.lahan.farmer.full_name

class Data_Pengajuan_Peminjaman (models.Model):
	bank_name = models.CharField(max_length=20, blank=True)
	no_rekening = models.CharField(max_length=30, blank=True)
	besar_peminjaman = models.CharField(max_length=20, blank=True)
	alasan_peminjaman = models.TextField(blank=True)
	tanggal_peminjaman = models.DateTimeField(blank=True)
	status = models.CharField(max_length=20, blank=True)
	alasan_penolakan = models.TextField(blank=True)
	farmer = models.ForeignKey(Pengguna)

	def __str__(self):
		return self.farmer.full_name

class Data_Lahan (models.Model):
	image_certificate = models.ImageField(upload_to='dataLahan/certificate', blank=True)
	farmer = models.ForeignKey(Pengguna)
	luas_lahan = models.CharField(max_length=20, blank=True)
	alamat_lahan = models.TextField(blank=True)
	keterangan = models.TextField(blank=True)
	tanggal_pengajuan = models.DateTimeField(blank=True)	

	def __str__(self):
		return self.farmer.full_name

class Data_Gambar_Lahan (models.Model):
	image = models.ImageField(upload_to='dataLahan/gambar', blank=True)
	gambar = models.CharField(max_length=20, blank=True)
	lahan = models.ForeignKey(Data_Lahan)

	def __str__(self):
		return self.lahan.farmer.full_name

class Data_Peminjaman (models.Model):
	bank_name = models.CharField(max_length=20, blank=True)
	no_rekening = models.CharField(max_length=30, blank=True)
	besar_peminjaman = models.CharField(max_length=20, blank=True)
	alasan_peminjaman = models.TextField(blank=True)
	tanggal_peminjaman = models.DateTimeField(blank=True)
	status = models.CharField(max_length=20, blank=True)	
	farmer = models.ForeignKey(Pengguna)

	def __str__(self):
		return self.farmer.full_name

class Data_Komposisi_Lahan (models.Model):
	nama_komposisi = models.CharField(max_length=50, blank=True)
	jenis_komposisi = models.CharField(max_length=50, blank=True)
	keterangan = models.TextField(blank=True)
	lahan = models.ForeignKey(Data_Lahan)

	def __str__(self):
		return self.lahan.farmer.full_name

class Data_Bibit_Pupuk (models.Model):
	nama_komponen = models.CharField(max_length=50, blank=True)
	jenis_komponen = models.CharField(max_length=50, blank=True)
	keterangan = models.TextField(blank=True)
	lahan = models.ForeignKey(Data_Lahan)

	def __str__(self):
		return self.lahan.farmer.full_name

class Data_Kegiatan_Pengolahan_Lahan (models.Model):
	nama_kegiatan = models.CharField(max_length=50, blank=True)	
	keterangan = models.TextField(blank=True)
	tanggal_mulai = models.DateTimeField(blank=True)
	tanggal_selesai = models.DateTimeField(blank=True, null=True)
	status = models.CharField(max_length=20, blank=True)
	lahan = models.ForeignKey(Data_Lahan)

	def __str__(self):
		return self.lahan.farmer.full_name

class Data_Estimasi_Tanam_Rawat_Panen(models.Model):
	nama_estimasi = models.CharField(max_length=50, blank=True)	
	keterangan = models.TextField(blank=True)
	tanggal_estimasi = models.DateField(blank=True)
	lahan = models.ForeignKey(Data_Lahan)

	def __str__(self):
		return self.lahan.farmer.full_name