from django.conf.urls import url
from farmer import views

app_name = 'farmer'

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^logout/$',views.logout,name='logout'),
	
	url(r'^create-pengajuan-lahan/',views.createPengajuanLahan, name='createPengajuanLahan'),
	url(r'^daftar-pengajuan-lahan/',views.daftarPengajuanLahan, name='daftarPengajuanLahan'),
	url(r'^ubah-pengajuan/(?P<id>\d+)/$',views.ubahPengajuan, name='ubahPengajuan'),
	url(r'^hapus-pengajuan/(?P<id>\d+)/$',views.hapusPengajuan, name='hapusPengajuan'),
	url(r'^hapus-pengajuan-tolak/(?P<id>\d+)/$',views.hapusPengajuanTolak, name='hapusPengajuanTolak'),
	url(r'^reject-pengajuan/(?P<id>\d+)/$',views.rejectPengajuan, name='rejectPengajuan'),
	url(r'^daftar-pengajuan-tolak/',views.daftarPengajuanLahanTolak, name='daftarPengajuanLahanTolak'),

	url(r'^create-peminjaman-uang/',views.createPeminjamanUang, name='createPeminjamanUang'),
	url(r'^daftar-peminjaman-uang/',views.daftarPeminjamanUang, name='daftarPeminjamanUang'),
	url(r'^ubah-peminjaman/(?P<id>\d+)/$',views.ubahPeminjaman, name='ubahPeminjaman'),
	url(r'^hapus-peminjaman/(?P<id>\d+)/$',views.hapusPeminjaman, name='hapusPeminjaman'),

	url(r'^daftar-peminjaman-setuju/',views.daftarPeminjamanSetuju, name='daftarPeminjamanSetuju'),
	url(r'^detail-peminjaman-setuju/(?P<id>\d+)/$',views.detailPeminjamanSetuju, name='detailPeminjamanSetuju'),
	url(r'^daftar-peminjaman-tolak/',views.daftarPeminjamanTolak, name='daftarPeminjamanTolak'),
	url(r'^detail-peminjaman-tolak/(?P<id>\d+)/$',views.detailPeminjamanTolak, name='detailPeminjamanTolak'),
	url(r'^hapus-peminjaman-tolak/(?P<id>\d+)/$',views.hapusPeminjamanTolak, name='hapusPeminjamanTolak'),

	url(r'^data-lahan/',views.indexDataLahan, name='indexDataLahan'),
	url(r'^detail-lahan/(?P<id>\d+)/$',views.detailLahan, name='detailLahan'),

	url(r'^data-diri/',views.indexDataDiri, name='indexDataDiri'),
	url(r'^ganti-foto/',views.gantiFoto, name='gantiFoto'),
	url(r'^ganti-profil/',views.gantiProfil, name='gantiProfil'),
	url(r'^ganti-password/',views.gantiPassword, name='gantiPassword'),
]