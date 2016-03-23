from django.contrib.auth.models import User
class GeneratePassword():

	def run (data):
		data['random_password']= User.objects.make_random_password()
	