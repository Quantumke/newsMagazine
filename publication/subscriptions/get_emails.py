class GetEmails():

	def run(request_data, data):
	   data['sub_data']=GetEmails.get_sub_data(request_data)




	def get_sub_data(request_data):
	   sub_data={}
	   sub_data['email']=request_data.get('email')
	   return sub_data
