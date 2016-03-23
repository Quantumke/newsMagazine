from publication.models import save_registration_transaction
from django.contrib.auth.models import User

class SaveRegTransaction():
	def run(data):
		user_data= data.get('user_data')
		reg_event={}
		reg_event['username']= user_data.get('username')
		reg_event['email']=user_data.get('email')
		reg_event['password']=(data.get('random_password'))
		reg_event['firstname']=user_data.get('first_name')
		reg_event['lastname']=user_data.get('last_name')
		save= save_registration_transaction(**reg_event)
		save.save()
