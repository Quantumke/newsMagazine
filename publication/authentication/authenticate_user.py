from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext


class AuthenticateUser():
	def run(request , data):
		login_data= data.get('login_data')
		logindata= User(**login_data)
		username = logindata.username
		password = logindata.password
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/login/')
			else:
				return HttpResponse("Password Valid but the account has been blocked")
		else:
			print("invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid username or password")
			
 