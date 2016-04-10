class GetFormData():
	def run(request_data,request_files, data):
		data['post_data']=GetFormData.get_post_data(request_data)
		data['files']=GetFormData.get_posted_image(request_files)
		#print (request_files)
	def get_post_data(request_data):
		post_data={}
		post_data['title']=request_data.get('title')
		post_data['body']= request_data.get('body')
		post_data['category']= request_data.get('category')
		post_data['image']=request_data.get('image')
		return post_data

	def get_posted_image(request_files):
		files={}
		files['image']=request_files.get('image')
		return files