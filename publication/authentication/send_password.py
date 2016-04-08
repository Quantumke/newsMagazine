from publication.models import save_registration_transaction
class SendPassword():

	def run(data):
		forgot=data.get('forgot')
		email=forgot.get('email')
		data['email']=email
		password=save_registration_transaction.objects.get(email=email)
		password=password.password
		data['password']=password
		#print(email,password)
		
		
