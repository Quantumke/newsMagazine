class GetDetails():
	def run (request_data,data):
		data['user_data']= GetDetails.get_data(request_data)

	def get_data(request_data):
		user_data = {}
		user_data['username']= request_data.get('username')
		user_data['email'] = request_data.get('email')
		user_data['first_name']= request_data.get('first_name')
		user_data['last_name']= request_data.get('last_name')
		return user_data