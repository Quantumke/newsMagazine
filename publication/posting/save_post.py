class SavePost():
	def run (data):
		post_data= data.get('post_data')
		generate_slug = data.get('generate_slug')
		print(generate_slug, post_data)
		
