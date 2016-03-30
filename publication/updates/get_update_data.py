class GetUpdateData():

	def run(request_data, data):
		data['update_data']=GetUpdateData.get_data(request_data)



	def get_data(request_data):
		update_data= {}
		update_data['title']= request_data.POST.get('title')
		update_data['body']= request_data.POST.get('body')
		update_data['category']= request_data.POST.get('category')
		return update_data
