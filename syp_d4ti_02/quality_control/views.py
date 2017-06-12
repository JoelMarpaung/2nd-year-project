from django.shortcuts import render,  redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.core.urlresolvers import reverse
from django.conf import settings
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import User
from staff.models import *
from farmer.models import *

# Create your views here.
@login_required(login_url=settings.LOGIN_ADMIN_URL)
def index(request):
	account = Staff.objects.get(username=request.session['username'],role='quality')
	return render(request,'quality_control/index.html', {'nbar':'home','account':account})

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def logout(request):
	account = Staff.objects.get(username=request.session['username'],role='quality')
	auth_logout(request)
	return redirect('/login-admin/')

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def indexDataLahan(request):
	account = Staff.objects.get(username=request.session['username'],role='quality')
	data_farmer = Pengguna.objects.all().order_by('-id')
	return render(request,'quality_control/data_lahan/index.html', {'nbar':'lahan', 'data_farmer':data_farmer,'account':account})

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def detailPetani(request, id):
	account = Staff.objects.get(username=request.session['username'],role='quality')
	data_farmer = Pengguna.objects.filter(id=id).order_by('-id')
	data_lahan = Data_Lahan.objects.filter(farmer_id=id).order_by('-id')
	paginator = Paginator(data_lahan, 5)
	page = request.GET.get('page')
	try:
		data_lahan = paginator.page(page)	
	except PageNotAnInteger:
		data_lahan = paginator.page(1)
	except EmptyPage:
		data_lahan = paginator.page(paginator.num_pages)
	return render(request,'quality_control/data_lahan/detail_petani.html', {'nbar':'lahan', 'data_farmer':data_farmer, 'data_lahan':data_lahan,'account':account})

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def detailLahan(request, id):
	account = Staff.objects.get(username=request.session['username'],role='quality')
	data_lahan = Data_Lahan.objects.filter(id=id).order_by('-id')
	data_gambar = Data_Gambar_Lahan.objects.filter(lahan_id=id).order_by('-id')
	data_kegiatan = Data_Kegiatan_Pengolahan_Lahan.objects.filter(lahan_id=id).order_by('-id')
	data_komposisi = Data_Komposisi_Lahan.objects.filter(lahan_id=id).order_by('-id')
	data_komponen = Data_Bibit_Pupuk.objects.filter(lahan_id=id).order_by('-id')
	data_estimasi = Data_Estimasi_Tanam_Rawat_Panen.objects.filter(lahan_id=id).order_by('-id')
	return render(request,'quality_control/data_lahan/detail_lahan.html', {'nbar':'lahan','data_lahan':data_lahan,'data_gambar':data_gambar, 'data_kegiatan':data_kegiatan, 'data_komposisi':data_komposisi, 'data_komponen':data_komponen, 'data_estimasi':data_estimasi,'account':account})

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def tambahKomposisi(request, id):
	account = Staff.objects.get(username=request.session['username'],role='quality')
	komposisi = Data_Komposisi_Lahan(
				nama_komposisi = request.POST['nama_komposisi'],				
				jenis_komposisi = request.POST['jenis_komposisi'],				
				keterangan = request.POST['keterangan'],				
				lahan_id = id,
		)
	komposisi.save()
	lahan = Data_Lahan.objects.get(id=komposisi.lahan_id)
	notif = Notifications(
			pengirim = 'Quality',
			judul = 'Tambah Komposisi Lahan',
			keterangan = 'Komposisi Lahan anda sudah ditambah yaitu, '+request.POST['nama_komposisi'],
			tanggal = datetime.datetime.now(),
			status = 'belum dibaca',
			farmer_id = lahan.farmer_id,
		)
	notif.save()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def hapusKomposisi(request, id):
	account = Staff.objects.get(username=request.session['username'],role='quality')
	komposisi = Data_Komposisi_Lahan.objects.filter(id=id)
	komposisi.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def tambahKomponen(request, id):
	account = Staff.objects.get(username=request.session['username'],role='quality')
	data_komponen = Data_Bibit_Pupuk(
				nama_komponen = request.POST['nama_komponen'],				
				jenis_komponen = request.POST['jenis_komponen'],				
				keterangan = request.POST['keterangan'],				
				lahan_id = id,
		)
	data_komponen.save()
	lahan = Data_Lahan.objects.get(id=data_komponen.lahan_id)
	notif = Notifications(
			pengirim = 'Quality',
			judul = 'Tambah Komponen Lahan',
			keterangan = 'Komponen Lahan anda sudah ditambah yaitu, '+request.POST['nama_komponen'],
			tanggal = datetime.datetime.now(),
			status = 'belum dibaca',
			farmer_id = lahan.farmer_id,
		)
	notif.save()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def hapusKomponen(request, id):
	account = Staff.objects.get(username=request.session['username'],role='quality')
	komposisi = Data_Bibit_Pupuk.objects.filter(id=id)
	komposisi.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def tambahEstimasi(request, id):
	account = Staff.objects.get(username=request.session['username'],role='quality')
	estimasi = Data_Estimasi_Tanam_Rawat_Panen(
				nama_estimasi = request.POST['nama_estimasi'],								
				keterangan = request.POST['keterangan'],				
				tanggal_estimasi = request.POST['tanggal_estimasi'],				
				lahan_id = id,
		)
	estimasi.save()
	lahan = Data_Lahan.objects.get(id=estimasi.lahan_id)
	notif = Notifications(
			pengirim = 'Quality',
			judul = 'Tambah Estimasi Lahan',
			keterangan = 'Estimasi Lahan anda sudah ditambah yaitu, '+request.POST['nama_estimasi'],
			tanggal = datetime.datetime.now(),
			status = 'belum dibaca',
			farmer_id = lahan.farmer_id,
		)
	notif.save()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def hapusEstimasi(request, id):
	account = Staff.objects.get(username=request.session['username'],role='quality')
	estimasi = Data_Estimasi_Tanam_Rawat_Panen.objects.filter(id=id)
	estimasi.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url=settings.LOGIN_ADMIN_URL)
def gantiPassword(request):
	if request.method == 'POST':
		user = User.objects.get(username=request.session['username'])
		user.set_password(request.POST['password1'])
		user.save()
		return redirect('/quality/ganti-password/')
	else:
		account = Staff.objects.get(username=request.session['username'],role='quality')
	return render(request,'quality_control/ganti_password.html', {'nbar':'home','account':account})