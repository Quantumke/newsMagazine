from publication.models import *
class SaveContactEvent():
	def run(data):
		contact_data= data.get('contact_data')
		name = contact_data.get('name')
		email= contact_data.get('email')
		message=contact_data.get('message')
		print(name, email, message)
		save= contact_event(name=name, email=email, message=message)
		save.save()
