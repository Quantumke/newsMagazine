from publication.models import *
class SaveSub():
	def run (data):
		sub_data= data.get('sub_data')
		email=sub_data.get('email')
		email= email
		save =subscribe(email=email)
		save.save()
		print(email)
		
