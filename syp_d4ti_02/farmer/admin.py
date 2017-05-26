from django.contrib import admin
from farmer.models import *
# Register your models here.

class PenggunaAdmin(admin.ModelAdmin):
	list_display = ['username','full_name','phone','kabupaten','kecamatan','alamat']
	list_filter = ('username','full_name','kabupaten','kecamatan')
	search_fields = ['username','full_name','kabupaten','kecamatan']
	list_per_page = 25

admin.site.register(Pengguna, PenggunaAdmin)


class AkunAdmin(admin.ModelAdmin):
	list_display = ['akun','pengguna','jenis_akun']
	list_filter = ('jenis_akun',)
	search_fields = []
	list_per_page = 25

admin.site.register(Akun, AkunAdmin)
