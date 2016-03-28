class GetContactDetails():
	def run(request_data, data):
		data['contact_data']= GetContactDetails.get_data(request_data)


	def get_data(request_data):
		contact_data= {}
		contact_data['name']= request_data.get('name')
		contact_data['email']= request_data.get('email')
		contact_data['message']= request_data.get('message')
		return  contact_data
