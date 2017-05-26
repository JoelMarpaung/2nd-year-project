from django.conf.urls import url
from surveyer import views

app_name = 'surveyer'
urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^logout/$',views.logout,name='logout'),
	url(r'^data-lahan/$',views.indexDataLahan, name='indexDataLahan'),
	url(r'^detail-petani/(?P<id>\d+)/$',views.detailPetani, name='detailPetani'),
	url(r'^detail-lahan/(?P<id>\d+)/$',views.detailLahan, name='detailLahan'),
	url(r'^tambah-kegiatan/(?P<id>\d+)/$',views.tambahKegiatan, name='tambahKegiatan'),
	url(r'^konfirmasi-kegiatan/(?P<id>\d+)/$',views.konfirmasiKegiatan, name='konfirmasiKegiatan'),
	url(r'^hapus-kegiatan/(?P<id>\d+)/$',views.hapusKegiatan, name='hapusKegiatan'),
	url(r'^ganti-password/',views.gantiPassword, name='gantiPassword'),
]