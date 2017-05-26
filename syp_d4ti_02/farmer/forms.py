from django.forms import ModelForm
from django import forms
from .models import *

class RegistrationForm(ModelForm):
	password = forms.CharField(label='Kata sandi', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Ulangi kata sandi', widget=forms.PasswordInput)
    username = forms.CharField(label='Nama Pengguna')

    class Meta:
    	model = (Pengguna)
    	fields = ['full_name','phone','kabupaten','kecamatan','alamat']
    	labels = {
    		'full_name':"Nama Lengkap",
    		'phone' : "No. Telepon",
    		'kabupaten' : "Kabupaten",
    		'kecamatan' : "Kecamatan",
    		'alamat' : "Alamat",
    	}
    	error_messages = {
    		'username':{
    			'required',
    			'min_length = 8'
    		}
    	}

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Kata sandi tidak sama!!!')
        return cd['password2']

