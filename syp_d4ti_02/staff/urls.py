from django.conf.urls import url
from staff import views

app_name = 'staff'

urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^logout/$',views.logout,name='logout'),
	url(r'^create-staff/$',views.createStaff, name='createStaff'),
	url(r'^daftar-staff/$',views.daftarStaff, name='daftarStaff'),
	url(r'^ubah-staff/(?P<id>\d+)/$',views.ubahStaff, name='ubahStaff'),
	url(r'^hapus-staff/(?P<id>\d+)/$',views.hapusStaff, name='hapusStaff'),
	
	url(r'^pending-pengajuan-lahan/$',views.pendingPengajuanLahan, name='pendingPengajuanLahan'),	
	url(r'^detail-pengajuan/(?P<id>\d+)/$',views.detailPengajuan, name='detailPengajuan'),
	url(r'^tolak-pengajuan/(?P<id>\d+)/$',views.tolakPengajuan, name='tolakPengajuan'),
	url(r'^terima-pengajuan/(?P<id>\d+)/$',views.terimaPengajuan, name='terimaPengajuan'),

	url(r'^reject-pengajuan-lahan/$',views.rejectPengajuanLahan, name='rejectPengajuanLahan'),
	url(r'^detail-pengajuan-reject/(?P<id>\d+)/$',views.detailPengajuanTolak, name='detailPengajuanTolak'),
	url(r'^hapus-pengajuan/(?P<id>\d+)/$',views.hapusPengajuan, name='hapusPengajuan'),
	
	url(r'^pending-peminjaman-uang/$',views.pendingPeminjamanUang, name='pendingPeminjamanUang'),
	url(r'^detail-peminjaman/(?P<id>\d+)/$',views.detailPeminjaman, name='detailPeminjaman'),
	url(r'^tolak-peminjaman/(?P<id>\d+)/$',views.tolakPeminjaman, name='tolakPeminjaman'),
	url(r'^terima-peminjaman/(?P<id>\d+)/$',views.terimaPeminjaman, name='terimaPeminjaman'),

	url(r'^accept-peminjaman-uang/$',views.acceptPeminjamanUang, name='acceptPeminjamanUang'),
	url(r'^detail-peminjaman-belum/(?P<id>\d+)/$',views.detailPeminjamanBelum, name='detailPeminjamanBelum'),
	url(r'^konfirmasi-peminjaman/(?P<id>\d+)/$',views.konfirmasiPeminjaman, name='konfirmasiPeminjaman'),
	url(r'^accept-peminjaman-uang-sudah/$',views.acceptPeminjamanUangSudah, name='acceptPeminjamanUangSudah'),
	url(r'^detail-peminjaman-sudah/(?P<id>\d+)/$',views.detailPeminjamanSudah, name='detailPeminjamanSudah'),
	url(r'^hapus-peminjaman-sudah/(?P<id>\d+)/$',views.hapusPeminjamanSudah, name='hapusPeminjamanSudah'),
	
	url(r'^reject-peminjaman-uang/$',views.rejectPeminjamanUang, name='rejectPeminjamanUang'),
	url(r'^detail-peminjaman-tolak/(?P<id>\d+)/$',views.detailPeminjamanTolak, name='detailPeminjamanTolak'),
	url(r'^hapus-peminjaman/(?P<id>\d+)/$',views.hapusPeminjaman, name='hapusPeminjaman'),

	url(r'^data-lahan/$',views.indexDataLahan, name='indexDataLahan'),
	url(r'^detail-petani/(?P<id>\d+)/$',views.detailPetani, name='detailPetani'),
	url(r'^detail-lahan/(?P<id>\d+)/$',views.detailLahan, name='detailLahan'),
	url(r'^ganti-password/',views.gantiPassword, name='gantiPassword'),
]