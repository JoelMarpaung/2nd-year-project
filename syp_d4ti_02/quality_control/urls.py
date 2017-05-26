from django.conf.urls import url
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^logout/$',views.logout,name='logout'),
	url(r'^data-lahan/$',views.indexDataLahan, name='indexDataLahan'),
	url(r'^detail-petani/(?P<id>\d+)/$',views.detailPetani, name='detailPetani'),
	url(r'^detail-lahan/(?P<id>\d+)/$',views.detailLahan, name='detailLahan'),
	url(r'^tambah-komposisi/(?P<id>\d+)/$',views.tambahKomposisi, name='tambahKomposisi'),
	url(r'^hapus-komposisi/(?P<id>\d+)/$',views.hapusKomposisi, name='hapusKomposisi'),
	url(r'^tambah-komponen/(?P<id>\d+)/$',views.tambahKomponen, name='tambahKomponen'),
	url(r'^hapus-komponen/(?P<id>\d+)/$',views.hapusKomponen, name='hapusKomponen'),
	url(r'^tambah-estimasi/(?P<id>\d+)/$',views.tambahEstimasi, name='tambahEstimasi'),
	url(r'^hapus-estimasi/(?P<id>\d+)/$',views.hapusEstimasi, name='hapusEstimasi'),
	url(r'^ganti-password/',views.gantiPassword, name='gantiPassword'),
]