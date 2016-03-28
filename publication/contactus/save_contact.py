from publication.models import *
class SaveContact():
	def run(data):
		contact_data= data.get('contact_data')
		name= contact_data.get('name')
		email= contact_data.get('email')
		message= contact_data.get('message')
		save= contact_us(name=name, email=email, message= message)
		save.save()

		#print(name, email, message)
