class GetChangePass():
	def run(request_data, data):
		data['reset_data']=GetChangePass.get_details(request_data)
		#print(request_data)

	def get_details(request_data):
		reset_data={}
		reset_data['email']=request_data.get('email')
		reset_data['password']=request_data.get('password')
		reset_data['new_password']=request_data.get('new_password')
		return reset_data
