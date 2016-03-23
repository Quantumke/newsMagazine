from publication.models import *
from django.contrib.auth.models import User
class SaveUser():
	def run (data):
		userdata= data.get('user_data')
		new_user= User(**userdata)
		password=(data.get('random_password'))
		# password=new_user.password
		new_user.set_password(password)
		new_user.save()
	
		# print(password, username)
