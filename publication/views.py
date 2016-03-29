from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth import logout
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
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
from .posting import save_post_transaction
from .subscriptions import get_emails
from .subscriptions import  save_sub
from .subscriptions import save_sub_event
from .contactus import get_contact_details
from .contactus import save_contact
from .contactus import save_contact_event
from .updates import get_update_data
from .updates import  save_update
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
		save_post_transaction.SavePostTransaction.run(data)


	return render(request, 'addpost.html', 
		{'post_data':post_data}, context_instance=RequestContext(request))

def view_post(request):
	return render_to_response('index.html',{
		'posts': news_posts.objects.all()})
def view_more(request, slug):
	return render_to_response('view-more.html', {
		'posts':get_object_or_404(news_posts, slug=slug)
		})

def subscriptions(request):
		context = RequestContext(request)
		sub = subscribes(data=request.POST)
		if request.method == 'POST':
			data = {}
			get_emails.GetEmails.run(request.POST, data)
			save_sub.SaveSub.run(data)
			save_sub_event.SaveSubEvent.run(data)


		return render(request, 'subscription.html',
					  {'sub': sub}, context_instance=RequestContext(request))

def contact(request):
		context = RequestContext(request)
		contact_form = contactus(data=request.POST)
		if request.method == 'POST':
			data = {}
			get_contact_details.GetContactDetails.run(request.POST, data)
			save_contact.SaveContact.run(data)
			save_contact_event.SaveContactEvent.run(data)



		return render(request, 'contact.html',
					  {'contact_form': contact_form}, context_instance=RequestContext(request))


def update_post(request, id):
		if id:
			instance =news_posts.objects.get(id=id)
			update_data = newadd(request.POST or None, instance=instance)
			if update_data.is_valid():
				data = {}
				get_update_data.GetUpdateData.run(request, data)
				save_update.SaveUpdate.run(data, id)


				return HttpResponseRedirect('/login/')
			context = {
				"title": instance.title,
				"instance": instance,
				"update_data":update_data,

			}




		return render(request, 'update.html',context)

