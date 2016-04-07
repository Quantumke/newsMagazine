from .models import *
from django.contrib.auth.models import User
from django import forms

class authentication(forms.ModelForm):

	class Meta:
		model= User
		fields =('username', 'password' , 'email', 'first_name', 'last_name')

class newadd(forms.ModelForm):

	class Meta:
		model = news_posts
		fields=('title', 'body', 'category')

class subscribes(forms.ModelForm):

	class Meta:
		model = subscribe
		fields =('email',)
class contactus(forms.ModelForm):

	class Meta:
		model=contact_us
		fields=('name', 'email', 'message',)

class resetpassword(forms.ModelForm):

	class Meta:
		model=forgotpassword
		fields=('email',)