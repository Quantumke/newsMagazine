class GetFormData():
	def run(request_data, data):
		data['post_data']=GetFormData.get_post_data(request_data)

	def get_post_data(request_data):
		post_data={}
		post_data['title']=request_data.get('title')
		post_data['body']= request_data.get('body')
		post_data['category']= request_data.get('category')
		return post_data