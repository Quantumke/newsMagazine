class ForgotPassword():

	def run(data):
		forgot=data.get('forgot')
		email=forgot.get('email')
		print(email)
