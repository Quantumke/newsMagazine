class GetForgotEmail():

	def run(request_data,data):
		data['forgot']=GetForgotEmail.get_details(request_data)
		#print(request_data)
		


	def get_details(request_data):
		forgot={}
		forgot['email']=request_data.get('email')
		return forgot
