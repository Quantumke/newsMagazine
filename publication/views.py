from django.shortcuts import render
from django.template import RequestContext
from .forms import *
from .authentication import get_details
from .authentication import generate_password
from .authentication import save_user
from .authentication import send_password_to_mail
from .authentication import save_reg_transaction

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

