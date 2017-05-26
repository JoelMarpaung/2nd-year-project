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
	account = Staff.objects.get(username=request.session['username'],role='admin')
	return render(request,'staff/index.html', {'nbar':'home','account':account})

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def logout(request):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	auth_logout(request)
	return redirect('/login-admin/')

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def createStaff(request):
	if request.method == 'POST':
		user = User(
				username = request.POST['username'],				
			)
		user.set_password(request.POST['password'],)
		user.save()
		staff = Staff(
				username = request.POST['username'],
				full_name = request.POST['full_name'],
				role = request.POST['role'],				
				photo = request.FILES['photo'],				
			) 
		staff.save()
		account = Akun_Staff(
				akun = User.objects.get(username=request.POST['username']),
				staff = Staff.objects.get(username=request.POST['username']),
				akun_id = User.objects.get(username=request.POST['username']).id,
				staff_id = Staff.objects.get(username=request.POST['username']).id,
				jenis_akun = request.POST['role'],				
			)
		account.save()
		return redirect('/staff/daftar-staff')
	else:		
		account = Staff.objects.get(username=request.session['username'],role='admin')
		return render(request, 'staff/data_staff/create.html', {'nbar':'activeStaff', 'li':'createStaff','account':account})

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def daftarStaff(request):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	daftar_staff = Staff.objects.all().order_by('-role')
	paginator = Paginator(daftar_staff, 5)
	page = request.GET.get('page')
	try:
		daftar_staff = paginator.page(page)	
	except PageNotAnInteger:
		daftar_staff = paginator.page(1)
	except EmptyPage:
		daftar_staff = paginator.page(paginator.num_pages)
	return render(request, 'staff/data_staff/daftar.html', {'nbar':'activeStaff', 'li':'daftarStaff', 'daftar_staff':daftar_staff,'account':account})

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def ubahStaff(request, id):
	if request.method == 'POST':		
		staff = Staff.objects.get(id=id)		
		staff.full_name = request.POST['full_name']
		staff.role = request.POST['role']
		staff.photo = request.FILES['photo']		
		staff.save()		
		account = Akun_Staff.objects.get(staff_id=id)
		account.jenis_akun = request.POST['role']		
		account.save()		
		return redirect('/staff/daftar-staff')
	else:		
		account = Staff.objects.get(username=request.session['username'],role='admin')
		daftar_staff = Staff.objects.filter(id=id)
	return render(request, 'staff/data_staff/detail.html', {'nbar':'activeStaff', 'li':'daftarStaff', 'daftar_staff':daftar_staff,'account':account})	

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def hapusStaff(request, id):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	staff = Staff.objects.get(id=id)
	staff.delete()
	return redirect('/staff/daftar-staff')		

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def pendingPengajuanLahan(request):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	pengajuan_pending = Data_Pengajuan_Lahan.objects.filter(status='pending').order_by('-tanggal_pengajuan') 
	paginator = Paginator(pengajuan_pending, 10)
	page = request.GET.get('page')
	try:
		pengajuan_pending = paginator.page(page)	
	except PageNotAnInteger:
		pengajuan_pending = paginator.page(1)
	except EmptyPage:
		pengajuan_pending = paginator.page(paginator.num_pages)
	return render(request, 'staff/pengajuan_lahan/pending.html', {'nbar':'activePengajuan', 'li':'pendingPengajuan', 'pengajuan_pending':pengajuan_pending,'account':account})

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def detailPengajuan(request, id):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	pengajuan_pending = Data_Pengajuan_Lahan.objects.filter(id=id)
	gambar_pending = Pengajuan_Gambar_Lahan.objects.filter(lahan_id=id)
	return render(request, 'staff/pengajuan_lahan/detail_pending.html', {'nbar':'activePengajuan', 'li':'pendingPengajuan', 'pengajuan_pending':pengajuan_pending, 'gambar_pending':gambar_pending,'account':account})

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def tolakPengajuan(request, id):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	pengajuan_tolak = Data_Pengajuan_Lahan.objects.get(id=id)
	pengajuan_tolak.alasan_penolakan = request.POST['alasan_penolakan']
	pengajuan_tolak.status = 'reject'
	pengajuan_tolak.save()
	return redirect('/staff/reject-pengajuan-lahan')		

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def terimaPengajuan(request, id):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	pengajuan_lahan = Data_Pengajuan_Lahan.objects.get(id=id)	
	create_lahan = Data_Lahan(
				image_certificate = pengajuan_lahan.image_certificate,
				luas_lahan = pengajuan_lahan.luas_lahan,
				alamat_lahan = pengajuan_lahan.alamat_lahan,				
				keterangan = pengajuan_lahan.keterangan,
				tanggal_pengajuan = datetime.datetime.now(),
				farmer_id = pengajuan_lahan.farmer_id,
			) 
	create_lahan.save()
	id_lahan = create_lahan.id	
	gambar1 = Pengajuan_Gambar_Lahan.objects.get(lahan_id=id,gambar='image1')
	image_lahan1 = Data_Gambar_Lahan(
				image = gambar1.image,
				lahan_id = id_lahan,
				gambar = 'image1',
			)
	image_lahan1.save()
	gambar2 = Pengajuan_Gambar_Lahan.objects.get(lahan_id=id,gambar='image2')
	image_lahan2 = Data_Gambar_Lahan(
				image = gambar2.image,
				lahan_id = id_lahan,
				gambar = 'image2',
			)
	image_lahan2.save()
	gambar3 = Pengajuan_Gambar_Lahan.objects.get(lahan_id=id,gambar='image3')
	image_lahan3 = Data_Gambar_Lahan(
				image = gambar3.image,
				lahan_id = id_lahan,
				gambar = 'image3',
			)
	image_lahan3.save()
	pengajuan_lahan = Data_Pengajuan_Lahan.objects.get(id=id)	
	pengajuan_lahan.delete()
	pengajuan_gambar = Pengajuan_Gambar_Lahan.objects.filter(lahan_id=id)
	pengajuan_gambar.delete()
	return redirect('/staff/pending-pengajuan-lahan')

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def rejectPengajuanLahan(request):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	pengajuan_reject = Data_Pengajuan_Lahan.objects.filter(status='reject').order_by('-tanggal_pengajuan')
	paginator = Paginator(pengajuan_reject, 5)
	page = request.GET.get('page')
	try:
		pengajuan_reject = paginator.page(page)	
	except PageNotAnInteger:
		pengajuan_reject = paginator.page(1)
	except EmptyPage:
		pengajuan_reject = paginator.page(paginator.num_pages)
	return render(request, 'staff/pengajuan_lahan/reject.html', {'nbar':'activePengajuan', 'li':'rejectPengajuan', 'pengajuan_reject':pengajuan_reject,'account':account})

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def detailPengajuanTolak(request, id):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	pengajuan_reject = Data_Pengajuan_Lahan.objects.filter(id=id)
	gambar_reject = Pengajuan_Gambar_Lahan.objects.filter(lahan_id=id)
	return render(request, 'staff/pengajuan_lahan/detail_tolak.html', {'nbar':'activePengajuan', 'li':'rejectPengajuan', 'pengajuan_reject':pengajuan_reject, 'gambar_reject':gambar_reject,'account':account})

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def hapusPengajuan(request, id):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	gambar_pending = Pengajuan_Gambar_Lahan.objects.filter(lahan_id=id)
	gambar_pending.delete()
	pengajuan_pending = Data_Pengajuan_Lahan.objects.filter(id=id)
	pengajuan_pending.delete()
	return redirect('/staff/reject-pengajuan-lahan')

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def pendingPeminjamanUang(request):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	peminjaman_uang = Data_Pengajuan_Peminjaman.objects.filter(status='pending').order_by('-tanggal_peminjaman')
	paginator = Paginator(peminjaman_uang, 5)
	page = request.GET.get('page')
	try:
		peminjaman_uang = paginator.page(page)	
	except PageNotAnInteger:
		peminjaman_uang = paginator.page(1)
	except EmptyPage:
		peminjaman_uang = paginator.page(paginator.num_pages)
	return render(request, 'staff/peminjaman_uang/pending.html', {'nbar':'activePeminjaman', 'li':'pendingPeminjaman', 'peminjaman_uang':peminjaman_uang,'account':account})

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def detailPeminjaman(request, id):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	peminjaman_uang = Data_Pengajuan_Peminjaman.objects.filter(id=id)
	return render(request, 'staff/peminjaman_uang/detail_pending.html', {'nbar':'activePeminjaman', 'li':'pendingPeminjaman', 'peminjaman_uang':peminjaman_uang,'account':account})

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def tolakPeminjaman(request, id):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	peminjaman_tolak = Data_Pengajuan_Peminjaman.objects.get(id=id)	
	peminjaman_tolak.alasan_penolakan = request.POST['alasan_penolakan']
	peminjaman_tolak.status = 'reject'
	peminjaman_tolak.save()
	return redirect('/staff/reject-peminjaman-uang')		

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def terimaPeminjaman(request, id):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	peminjaman_uang = Data_Pengajuan_Peminjaman.objects.get(id=id)
	data_peminjaman = Data_Peminjaman(
						bank_name = peminjaman_uang.bank_name,
						no_rekening = peminjaman_uang.no_rekening,
						besar_peminjaman = peminjaman_uang.besar_peminjaman,
						alasan_peminjaman = peminjaman_uang.alasan_peminjaman,
						tanggal_peminjaman = datetime.datetime.now(),
						status = 'belumpinjam',
						farmer_id = peminjaman_uang.farmer_id,
		)
	data_peminjaman.save()	
	peminjaman_uang.delete()
	return redirect('/staff/accept-peminjaman-uang')		

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def acceptPeminjamanUang(request):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	peminjaman_uang = Data_Peminjaman.objects.filter(status='belumpinjam').order_by('-tanggal_peminjaman')
	paginator = Paginator(peminjaman_uang, 5)
	page = request.GET.get('page')
	try:
		peminjaman_uang = paginator.page(page)	
	except PageNotAnInteger:
		peminjaman_uang = paginator.page(1)
	except EmptyPage:
		peminjaman_uang = paginator.page(paginator.num_pages)
	return render(request, 'staff/peminjaman_uang/accept.html', {'nbar':'activePeminjaman', 'li':'acceptPeminjaman', 'peminjaman_uang':peminjaman_uang,'account':account})

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def detailPeminjamanBelum(request, id):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	peminjaman_uang = Data_Peminjaman.objects.filter(id=id)
	return render(request, 'staff/peminjaman_uang/detail_belum.html', {'nbar':'activePeminjaman', 'li':'acceptPeminjaman', 'peminjaman_uang':peminjaman_uang,'account':account})

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def konfirmasiPeminjaman(request, id):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	peminjaman_uang = Data_Peminjaman.objects.get(id=id)
	peminjaman_uang.status = 'sudahpinjam'
	peminjaman_uang.tanggal_peminjaman = datetime.datetime.now()
	peminjaman_uang.save()
	return redirect('/staff/accept-peminjaman-uang')

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def acceptPeminjamanUangSudah(request):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	peminjaman_uang = Data_Peminjaman.objects.filter(status='sudahpinjam').order_by('-tanggal_peminjaman')
	paginator = Paginator(peminjaman_uang, 5)
	page = request.GET.get('page')
	try:
		peminjaman_uang = paginator.page(page)	
	except PageNotAnInteger:
		peminjaman_uang = paginator.page(1)
	except EmptyPage:
		peminjaman_uang = paginator.page(paginator.num_pages)
	return render(request, 'staff/peminjaman_uang/accept_sudah.html', {'nbar':'activePeminjaman', 'li':'acceptPeminjaman', 'peminjaman_uang':peminjaman_uang,'account':account})

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def detailPeminjamanSudah(request, id):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	peminjaman_uang = Data_Peminjaman.objects.filter(id=id)
	return render(request, 'staff/peminjaman_uang/detail_sudah.html', {'nbar':'activePeminjaman', 'li':'acceptPeminjaman', 'peminjaman_uang':peminjaman_uang,'account':account})

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def hapusPeminjamanSudah(request, id):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	peminjaman_uang = Data_Peminjaman.objects.get(id=id)
	peminjaman_uang.delete()
	return redirect('/staff/accept-peminjaman-uang-sudah')		

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def rejectPeminjamanUang(request):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	peminjaman_uang = Data_Pengajuan_Peminjaman.objects.filter(status='reject').order_by('-tanggal_peminjaman')
	paginator = Paginator(peminjaman_uang, 5)
	page = request.GET.get('page')
	try:
		peminjaman_uang = paginator.page(page)	
	except PageNotAnInteger:
		peminjaman_uang = paginator.page(1)
	except EmptyPage:
		peminjaman_uang = paginator.page(paginator.num_pages)
	return render(request, 'staff/peminjaman_uang/reject.html', {'nbar':'activePeminjaman', 'li':'rejectPeminjaman', 'peminjaman_uang':peminjaman_uang,'account':account})

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def detailPeminjamanTolak(request, id):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	peminjaman_uang = Data_Pengajuan_Peminjaman.objects.filter(id=id)
	return render(request, 'staff/peminjaman_uang/detail_reject.html', {'nbar':'activePeminjaman', 'li':'rejectPeminjaman', 'peminjaman_uang':peminjaman_uang,'account':account})

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def hapusPeminjaman(request, id):	
	account = Staff.objects.get(username=request.session['username'],role='admin')
	peminjaman_uang = Data_Pengajuan_Peminjaman.objects.filter(id=id)
	peminjaman_uang.delete()
	return redirect('/staff/reject-peminjaman-uang')

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def indexDataLahan(request):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	data_farmer = Pengguna.objects.all()
	return render(request,'staff/data_lahan/index.html', {'nbar':'lahan', 'data_farmer':data_farmer,'account':account})

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def detailPetani(request, id):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	data_farmer = Pengguna.objects.filter(id=id)
	data_lahan = Data_Lahan.objects.filter(farmer_id=id)
	paginator = Paginator(data_lahan, 5)
	page = request.GET.get('page')
	try:
		data_lahan = paginator.page(page)	
	except PageNotAnInteger:
		data_lahan = paginator.page(1)
	except EmptyPage:
		data_lahan = paginator.page(paginator.num_pages)
	return render(request,'staff/data_lahan/detail_petani.html', {'nbar':'lahan', 'data_farmer':data_farmer, 'data_lahan':data_lahan,'account':account})

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def detailLahan(request, id):
	account = Staff.objects.get(username=request.session['username'],role='admin')
	data_lahan = Data_Lahan.objects.filter(id=id)
	data_gambar = Data_Gambar_Lahan.objects.filter(lahan_id=id)
	data_kegiatan = Data_Kegiatan_Pengolahan_Lahan.objects.filter(lahan_id=id).order_by('-id')
	data_komposisi = Data_Komposisi_Lahan.objects.filter(lahan_id=id).order_by('-id')
	data_komponen = Data_Bibit_Pupuk.objects.filter(lahan_id=id).order_by('-id')
	data_estimasi = Data_Estimasi_Tanam_Rawat_Panen.objects.filter(lahan_id=id).order_by('-id')
	return render(request,'staff/data_lahan/detail_lahan.html', {'nbar':'lahan','data_lahan':data_lahan,'data_gambar':data_gambar, 'data_kegiatan':data_kegiatan, 'data_komposisi':data_komposisi, 'data_komponen':data_komponen, 'data_estimasi':data_estimasi,'account':account})

@login_required(login_url=settings.LOGIN_ADMIN_URL)
def gantiPassword(request):
	if request.method == 'POST':
		user = User.objects.get(username=request.session['username'])
		user.set_password(request.POST['password1'])
		user.save()
		return redirect('/staff/ganti-password/')
	else:
		account = Staff.objects.get(username=request.session['username'],role='admin')
	return render(request,'staff/ganti_password.html', {'nbar':'home','account':account})