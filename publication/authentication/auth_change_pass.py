from publication.models import  save_registration_transaction
from django.contrib.auth.models import User

class AuthChangePass():
	def run(data):
		reset_data=data.get('reset_data')
		#print(reset_data)
		#update_pass=User(**reset_data)
		email=reset_data.get('email')
		old_password=reset_data.get('password')
		password=reset_data.get('new_password')
		update=User.objects.get(email=email)
		update.set_password(password)
		update.save()
