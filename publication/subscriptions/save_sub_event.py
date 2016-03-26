from publication.models import *
class SaveSubEvent():
	def run(data):
		sub_data= data.get('sub_data')
		email=sub_data.get('email')
		save =subscribe_event(email=email)
		save.save()
		
