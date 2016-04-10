from publication.models import post_transaction
class SavePostTransaction():
	def run(data):
		post_data= data.get('post_data')
		postdata = post_transaction(**post_data)
		slug = data.get('slug')
		title = post_data.get('title')
		body = post_data.get('body')
		category=post_data.get('category')
		slug_data=slug.get('slug_data')
		image=post_data.get('image')
		print(title, body, category, slug_data)
		e = post_transaction(title=title, body=body, category=category, slug=slug_data, posted_by='ben', image=image)
		e.save()
		data['postdata']=postdata


		
