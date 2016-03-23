from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth import logout
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from .authentication import get_details
from .authentication import generate_password
from .authentication import save_user
from .authentication import send_password_to_mail
from .authentication import save_reg_transaction
from .authentication import get_login_details
from .authentication import authenticate_user
from .posting import get_form_data
from .posting import generate_extra_details
from .posting import save_post

# Create your views here.
def register_user(request):
	context = RequestContext(request)
	registered = False
	user_details = authentication(data=request.POST)
	if request.method == 'POST':
		data = {}
		get_details.GetDetails.run(request.POST, data)
		generate_password.GeneratePassword.run(data)
		save_user.SaveUser.run(data)
		send_password_to_mail.SendPasswordToMail.run(data)
		save_reg_transaction.SaveRegTransaction.run(data)

	return render(request,
		'register.html', {'user_details':user_details, 'registered':registered
		}, context_instance=RequestContext(request))

def login_user(request):
	context = RequestContext(request)
	if request.method=='POST':
		data={}
		get_login_details.GetLoginDetails.run(request.POST, data)
		authenticate_user.AuthenticateUser.run(request, data)

	return render(request, 'login.html',
		{}, context_instance=RequestContext(request))

def logout_user(request):
	logout(request)

	return HttpResponseRedirect('/login/')

def add_post(request):
	context = RequestContext(request)
	post_data=newadd(data=request.POST)
	if request.method=='POST':
		data ={}
		get_form_data.GetFormData.run(request.POST, data)
		generate_extra_details.GenerateExtraDetails.run(request,data)
		save_post.SavePost.run(data)


	return render(request, 'addpost.html', 
		{'post_data':post_data}, context_instance=RequestContext(request))

