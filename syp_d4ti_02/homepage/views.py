from django.shortcuts import render,  redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.core.urlresolvers import reverse
from django.conf import settings
# from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import User
from farmer.models import *
from staff.models import *

# Create your views here.
def register(request):
	if request.method == 'POST':
		user = User(
				username = request.POST['username'],				
			)
		user.set_password(request.POST['password'],)
		user.save()
		farmer = Pengguna(
				username = request.POST['username'],
				full_name = request.POST['full_name'],
				phone = request.POST['phone'],								
				kabupaten = request.POST['kabupaten'],
				kecamatan = request.POST['kecamatan'],
				alamat = request.POST['alamat'],							
				photo = 'unknown.png',
			) 
		farmer.save()
		account = Akun(
				akun = User.objects.get(username=request.POST['username']),
				pengguna = Pengguna.objects.get(username=request.POST['username']),
				akun_id = User.objects.get(username=request.POST['username']).id,
				pengguna_id = Pengguna.objects.get(username=request.POST['username']).id,
				jenis_akun = "farmer",				
			)
		account.save()
		return redirect('/login')
	else:
		return render(request,'homepage/register.html')

def loginAdmin(request):
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				staff = Staff.objects.get(username=request.POST.get('username'))
				auth_login(request, user)											
				request.session['username'] = request.POST['username']					
				if staff.role == 'admin':
					return redirect('/staff')	
				elif staff.role == 'surveyer': 
					return redirect('/surveyer')
				else:	
					return redirect('/quality')
			else:
				print("Account Not Active")
		else:
			print("Account Not Active")
	else:
		return render(request,'homepage/login_admin.html') 

def login(request):
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				akun = Akun.objects.get(akun_id=user.id)
				auth_login(request, user)				
				request.session['pengguna_id'] = akun.pengguna.id				
				request.session['username'] = request.POST['username']					
				return redirect('/')	
			else:
				print("Account Not Active")
		else:
			print("Account Not Active")
	else:
		return render(request,'homepage/login.html') 