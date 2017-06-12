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

from farmer.models import *
from django.contrib import messages

@login_required(login_url=settings.LOGIN_URL)
def logout(request):
	auth_logout(request)
	return redirect('/')

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def index(request):
	account = Pengguna.objects.get(username=request.session['username'])
	notifs = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca')
	num = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca').count()	
	return render(request, 'farmer/index.html', {'nbar':'home', 'farmer':account, 'notifs':notifs, 'num':num})

@login_required(login_url=settings.LOGIN_URL)
def createPengajuanLahan(request):
	if request.method == 'POST':
		pengajuan_lahan = Data_Pengajuan_Lahan(
				image_certificate = request.FILES['image_certificate'],
				luas_lahan = request.POST['luas_lahan'],
				alamat_lahan = request.POST['alamat_lahan'],
				status = 'pending',
				keterangan = request.POST['keterangan'],
				tanggal_pengajuan = datetime.datetime.now(),
				farmer_id = Pengguna.objects.get(username=request.session['username']).id,
			) 
		pengajuan_lahan.save()
		id_lahan = pengajuan_lahan.id
		image_lahan1 = Pengajuan_Gambar_Lahan(
				image = request.FILES['image1'],
				lahan_id = id_lahan,
				gambar = 'image1',
			)
		image_lahan1.save()
		image_lahan2 = Pengajuan_Gambar_Lahan(
				image = request.FILES['image2'],
				lahan_id = id_lahan,
				gambar = 'image2',
			)
		image_lahan2.save()
		image_lahan3 = Pengajuan_Gambar_Lahan(
				image = request.FILES['image3'],
				lahan_id = id_lahan,
				gambar = 'image3',
			)
		image_lahan3.save()
		return redirect('/daftar-pengajuan-lahan')
	else:
		account = Pengguna.objects.get(username=request.session['username'])
		notifs = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca')
		num = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca').count()	
	return render(request, 'farmer/pengajuan_lahan/create.html', 
		{'nbar':'activePengajuan', 'li':'createPengajuan', 'farmer':account, 'notifs':notifs, 'num':num})
	

@login_required(login_url=settings.LOGIN_URL)
def daftarPengajuanLahan(request):
	account = Pengguna.objects.get(username=request.session['username'])
	pengajuan_pending = Data_Pengajuan_Lahan.objects.filter(status='pending', farmer_id = Pengguna.objects.get(username=request.session['username']).id).order_by('-tanggal_pengajuan')
	paginator = Paginator(pengajuan_pending, 5)
	page = request.GET.get('page')
	try:
		pengajuan_pending = paginator.page(page)	
	except PageNotAnInteger:
		pengajuan_pending = paginator.page(1)
	except EmptyPage:
		pengajuan_pending = paginator.page(paginator.num_pages)
	notifs = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca')
	num = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca').count()	
	return render(request, 'farmer/pengajuan_lahan/daftar.html', 
		{'nbar':'activePengajuan', 'li':'daftarPengajuan', 'farmer':account, 'pengajuan_pending':pengajuan_pending, 'notifs':notifs, 'num':num})

@login_required(login_url=settings.LOGIN_URL)
def daftarPengajuanLahanTolak(request):
	account = Pengguna.objects.get(username=request.session['username'])
	pengajuan_reject = Data_Pengajuan_Lahan.objects.filter(status='reject', farmer_id = Pengguna.objects.get(username=request.session['username']).id).order_by('-tanggal_pengajuan')
	paginator = Paginator(pengajuan_reject, 5)
	page = request.GET.get('page')
	try:
		pengajuan_reject = paginator.page(page)	
	except PageNotAnInteger:
		pengajuan_reject = paginator.page(1)
	except EmptyPage:
		pengajuan_reject = paginator.page(paginator.num_pages)
	notifs = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca')
	num = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca').count()	
	return render(request, 'farmer/pengajuan_lahan/tolak.html', 
		{'nbar':'activePengajuan', 'li':'daftarPengajuan', 'farmer':account, 'pengajuan_reject':pengajuan_reject, 'notifs':notifs, 'num':num})

@login_required(login_url=settings.LOGIN_URL)
def ubahPengajuan(request, id):
	if request.method == 'POST':
		pengajuan_lahan = Data_Pengajuan_Lahan.objects.get(id=id)
		pengajuan_lahan.image_certificate = request.FILES['image_certificate']
		pengajuan_lahan.luas_lahan = request.POST['luas_lahan']
		pengajuan_lahan.alamat_lahan = request.POST['alamat_lahan']
		pengajuan_lahan.keterangan = request.POST['keterangan']
		pengajuan_lahan.tanggal_pengajuan = datetime.datetime.now()
		pengajuan_lahan.save()

		image_lahan1 = Pengajuan_Gambar_Lahan.objects.get(lahan_id=id, gambar='image1')
		image_lahan1.image = request.FILES['image1']
		image_lahan1.save()

		image_lahan2 = Pengajuan_Gambar_Lahan.objects.get(lahan_id=id, gambar='image2')
		image_lahan2.image = image = request.FILES['image2']
		image_lahan2.save()

		image_lahan3 = Pengajuan_Gambar_Lahan.objects.get(lahan_id=id, gambar='image3')
		image_lahan3.image = request.FILES['image3']
		image_lahan3.save()

		return redirect('/daftar-pengajuan-lahan')
	else :
		account = Pengguna.objects.get(username=request.session['username'])
		pengajuan_pending = Data_Pengajuan_Lahan.objects.filter(id=id)
		gambar_pending = Pengajuan_Gambar_Lahan.objects.filter(lahan_id=id)
	notifs = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca')
	num = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca').count()	
	return render(request, 'farmer/pengajuan_lahan/detail_pending.html', 
		{'nbar':'activePengajuan', 'li':'daftarPengajuan', 'farmer':account, 'pengajuan_pending':pengajuan_pending, 'gambar_pending':gambar_pending, 'notifs':notifs, 'num':num})

@login_required(login_url=settings.LOGIN_URL)
def rejectPengajuan(request, id):
	account = Pengguna.objects.get(username=request.session['username'])
	pengajuan_reject = Data_Pengajuan_Lahan.objects.filter(id=id)
	gambar_reject = Pengajuan_Gambar_Lahan.objects.filter(lahan_id=id)
	notifs = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca')
	num = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca').count()	
	return render(request, 'farmer/pengajuan_lahan/detail_tolak.html', 
		{'nbar':'activePengajuan', 'li':'daftarPengajuan', 'farmer':account, 'pengajuan_reject':pengajuan_reject, 'gambar_reject':gambar_reject, 'notifs':notifs, 'num':num})

@login_required(login_url=settings.LOGIN_URL)
def hapusPengajuan(request, id):
	gambar_pending = Pengajuan_Gambar_Lahan.objects.filter(lahan_id=id)
	gambar_pending.delete()
	pengajuan_pending = Data_Pengajuan_Lahan.objects.filter(id=id)
	pengajuan_pending.delete()
	return redirect('/daftar-pengajuan-lahan')

@login_required(login_url=settings.LOGIN_URL)
def hapusPengajuanTolak(request, id):	
	gambar_reject = Pengajuan_Gambar_Lahan.objects.filter(lahan_id=id)	
	gambar_reject.delete()
	pengajuan_reject = Data_Pengajuan_Lahan.objects.filter(id=id)	
	pengajuan_reject.delete()
	return redirect('/daftar-pengajuan-tolak')

@login_required(login_url=settings.LOGIN_URL)
def createPeminjamanUang(request):
	if request.method == 'POST':
		pengajuan_peminjaman = Data_Pengajuan_Peminjaman(
				bank_name = request.POST['bank_name'],
				no_rekening = request.POST['no_rekening'],
				besar_peminjaman = request.POST['besar_peminjaman'],
				alasan_peminjaman = request.POST['alasan_peminjaman'],				
				tanggal_peminjaman = datetime.datetime.now(),
				status = 'pending',			
				farmer_id = Pengguna.objects.get(username=request.session['username']).id,
			) 
		pengajuan_peminjaman.save()		
		return redirect('/daftar-peminjaman-uang')
	else:
		account = Pengguna.objects.get(username=request.session['username'])
	notifs = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca')
	num = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca').count()	
	return render(request, 'farmer/peminjaman_uang/create.html', {'nbar':'activePeminjaman', 'li':'createPeminjaman', 'farmer':account, 'notifs':notifs, 'num':num})

@login_required(login_url=settings.LOGIN_URL)
def daftarPeminjamanUang(request):
	account = Pengguna.objects.get(username=request.session['username'])
	peminjaman_uang = Data_Pengajuan_Peminjaman.objects.filter(status='pending', farmer_id = Pengguna.objects.get(username=request.session['username']).id).order_by('-tanggal_peminjaman')
	paginator = Paginator(peminjaman_uang, 5)
	page = request.GET.get('page')
	try:
		peminjaman_uang = paginator.page(page)	
	except PageNotAnInteger:
		peminjaman_uang = paginator.page(1)
	except EmptyPage:
		peminjaman_uang = paginator.page(paginator.num_pages)
	notifs = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca')
	num = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca').count()	
	return render(request, 'farmer/peminjaman_uang/daftar.html', {'nbar':'activePeminjaman', 'li':'daftarPeminjaman', 'farmer':account, 'peminjaman_uang':peminjaman_uang, 'notifs':notifs, 'num':num})

@login_required(login_url=settings.LOGIN_URL)
def ubahPeminjaman(request, id):
	if request.method == 'POST':
		pengajuan_peminjaman = Data_Pengajuan_Peminjaman.objects.get(id=id)
		pengajuan_peminjaman.bank_name = request.POST['bank_name']
		pengajuan_peminjaman.no_rekening = request.POST['no_rekening']
		pengajuan_peminjaman.besar_peminjaman = request.POST['besar_peminjaman']
		pengajuan_peminjaman.alasan_peminjaman = request.POST['alasan_peminjaman']
		pengajuan_peminjaman.tanggal_peminjaman = datetime.datetime.now()		
		pengajuan_peminjaman.save()		
		return redirect('/daftar-peminjaman-uang')
	else : 
		account = Pengguna.objects.get(username=request.session['username'])
		peminjaman_uang = Data_Pengajuan_Peminjaman.objects.filter(id=id)
	notifs = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca')
	num = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca').count()	
	return render(request, 'farmer/peminjaman_uang/detail_pending.html', {'nbar':'activePeminjaman', 'li':'daftarPeminjaman', 'farmer':account, 'peminjaman_uang':peminjaman_uang, 'notifs':notifs, 'num':num})

@login_required(login_url=settings.LOGIN_URL)
def hapusPeminjaman(request, id):
	peminjaman_uang = Data_Pengajuan_Peminjaman.objects.filter(id=id)
	peminjaman_uang.delete()
	return redirect('/daftar-peminjaman-uang')

@login_required(login_url=settings.LOGIN_URL)
def daftarPeminjamanSetuju(request):
	account = Pengguna.objects.get(username=request.session['username'])
	peminjaman_uang = Data_Peminjaman.objects.filter(farmer_id=account.id).order_by('-status')
	paginator = Paginator(peminjaman_uang, 5)
	page = request.GET.get('page')
	try:
		peminjaman_uang = paginator.page(page)	
	except PageNotAnInteger:
		peminjaman_uang = paginator.page(1)
	except EmptyPage:
		peminjaman_uang = paginator.page(paginator.num_pages)
	notifs = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca')
	num = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca').count()	
	return render(request, 'farmer/peminjaman_uang/setuju.html', {'nbar':'activePeminjaman', 'li':'daftarPeminjaman', 'farmer':account, 'peminjaman_uang':peminjaman_uang, 'notifs':notifs, 'num':num})

@login_required(login_url=settings.LOGIN_URL)
def detailPeminjamanSetuju(request, id):
	account = Pengguna.objects.get(username=request.session['username'])
	peminjaman_uang = Data_Peminjaman.objects.filter(id=id)	
	notifs = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca')
	num = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca').count()	
	return render(request, 'farmer/peminjaman_uang/detail_sudah.html', {'nbar':'activePeminjaman', 'li':'daftarPeminjaman', 'farmer':account, 'peminjaman_uang':peminjaman_uang, 'notifs':notifs, 'num':num})	

@login_required(login_url=settings.LOGIN_URL)
def daftarPeminjamanTolak(request):
	account = Pengguna.objects.get(username=request.session['username'])
	peminjaman_uang = Data_Pengajuan_Peminjaman.objects.filter(status='tolak', farmer_id = Pengguna.objects.get(username=request.session['username']).id).order_by('-tanggal_peminjaman')
	paginator = Paginator(peminjaman_uang, 1)
	page = request.GET.get('page')
	try:
		peminjaman_uang = paginator.page(page)	
	except PageNotAnInteger:
		peminjaman_uang = paginator.page(1)
	except EmptyPage:
		peminjaman_uang = paginator.page(paginator.num_pages)
	notifs = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca')
	num = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca').count()	
	return render(request, 'farmer/peminjaman_uang/tolak.html', {'nbar':'activePeminjaman', 'li':'daftarPeminjaman', 'farmer':account, 'peminjaman_uang':peminjaman_uang, 'notifs':notifs, 'num':num})	

@login_required(login_url=settings.LOGIN_URL)
def detailPeminjamanTolak(request, id):
	account = Pengguna.objects.get(username=request.session['username'])
	peminjaman_uang = Data_Pengajuan_Peminjaman.objects.filter(id=id)	
	notifs = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca')
	num = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca').count()	
	return render(request, 'farmer/peminjaman_uang/detail_tolak.html', {'nbar':'activePeminjaman', 'li':'daftarPeminjaman', 'farmer':account, 'peminjaman_uang':peminjaman_uang, 'notifs':notifs, 'num':num})	

@login_required(login_url=settings.LOGIN_URL)
def hapusPeminjamanTolak(request, id):
	peminjaman_uang = Data_Pengajuan_Peminjaman.objects.filter(id=id)
	peminjaman_uang.delete()
	return redirect('/daftar-peminjaman-tolak')

@login_required(login_url=settings.LOGIN_URL)
def indexDataLahan(request):
	account = Pengguna.objects.get(username=request.session['username'])
	data_lahan = Data_Lahan.objects.filter(farmer_id=account.id)
	paginator = Paginator(data_lahan, 5)
	page = request.GET.get('page')
	try:
		data_lahan = paginator.page(page)	
	except PageNotAnInteger:
		data_lahan = paginator.page(1)
	except EmptyPage:
		data_lahan = paginator.page(paginator.num_pages)
	notifs = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca')
	num = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca').count()	
	return render(request, 'farmer/data_lahan/index.html', {'nbar':'lahan', 'farmer':account, 'data_lahan':data_lahan, 'notifs':notifs, 'num':num})


@login_required(login_url=settings.LOGIN_URL)
def detailLahan(request, id):
	account = Pengguna.objects.get(username=request.session['username'])
	data_lahan = Data_Lahan.objects.filter(id=id)
	data_gambar = Data_Gambar_Lahan.objects.filter(lahan_id=id)
	data_kegiatan = Data_Kegiatan_Pengolahan_Lahan.objects.filter(lahan_id=id).order_by('-id')
	data_komposisi = Data_Komposisi_Lahan.objects.filter(lahan_id=id).order_by('-id')
	data_komponen = Data_Bibit_Pupuk.objects.filter(lahan_id=id).order_by('-id')
	data_estimasi = Data_Estimasi_Tanam_Rawat_Panen.objects.filter(lahan_id=id).order_by('-id')
	notifs = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca')
	num = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca').count()	
	return render(request,'farmer/data_lahan/detail_lahan.html', {'nbar':'lahan', 'farmer':account,'data_lahan':data_lahan,'data_gambar':data_gambar, 'data_kegiatan':data_kegiatan, 'data_komposisi':data_komposisi, 'data_komponen':data_komponen, 'data_estimasi':data_estimasi, 'notifs':notifs, 'num':num})


@login_required(login_url=settings.LOGIN_URL)
def indexDataDiri(request):
	account = Pengguna.objects.get(username=request.session['username'])
	notifs = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca')
	num = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca').count()	
	return render(request, 'farmer/profil/index.html', {'farmer':account, 'notifs':notifs, 'num':num})


@login_required(login_url=settings.LOGIN_URL)
def gantiFoto(request):
	account = Pengguna.objects.get(username=request.session['username'])
	account.photo = request.FILES['photo']					
	account.save()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url=settings.LOGIN_URL)
def gantiProfil(request):
	account = Pengguna.objects.get(username=request.session['username'])
	account.full_name = request.POST['full_name']					
	account.phone = request.POST['phone']
	account.kabupaten = request.POST['kabupaten']
	account.kecamatan = request.POST['kecamatan']
	account.alamat = request.POST['alamat']
	account.save()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url=settings.LOGIN_URL)
def gantiPassword(request):
	account = Pengguna.objects.get(username=request.session['username'])
	user = User.objects.get(username=request.session['username'])	
	user.set_password(request.POST['password1'])
	user.save()
	messages.add_message(request, messages.INFO, 'Password berhasil diganti')			
	return HttpResponseRedirect('/data-diri/')		

@login_required(login_url=settings.LOGIN_URL)
def notifications(request):
	account = Pengguna.objects.get(username=request.session['username'])
	notifs = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca')
	num = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca').count()	
	notifications = Notifications.objects.filter(farmer_id=account.id).order_by('status','-id') 
	paginator = Paginator(notifications, 10)
	page = request.GET.get('page')
	try:
		notifications = paginator.page(page)	
	except PageNotAnInteger:
		notifications = paginator.page(1)
	except EmptyPage:
		notifications = paginator.page(paginator.num_pages)
	return render(request,'farmer/notification/index.html', {'farmer':account, 'notifications':notifications, 'notifs':notifs, 'num':num})

@login_required(login_url=settings.LOGIN_URL)
def detailNotifications(request,id):
	account = Pengguna.objects.get(username=request.session['username'])
	notifs = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca')
	num = Notifications.objects.filter(farmer_id=account.id, status='belum dibaca').count()	
	notifications = Notifications.objects.filter(id=id)
	notification = Notifications.objects.get(id=id)
	notification.status = 'sudah dibaca'
	notification.save()
	return render(request,'farmer/notification/detail.html', {'farmer':account, 'notifications':notifications, 'notifs':notifs, 'num':num})

@login_required(login_url=settings.LOGIN_URL)
def deleteNotifications(request,id):
	account = Pengguna.objects.get(username=request.session['username'])
	notification = Notifications.objects.get(id=id)
	notification.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))