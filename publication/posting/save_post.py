from publication.models import news_posts
class SavePost():
	def run (data):
		post_data= data.get('post_data')
		#image=post_data.get('image')
		postdata = news_posts(**post_data)
		slug = data.get('slug')
		postdata=news_posts(**post_data)
		files=data.get('files')
		image=files.get('image')
		title = postdata.title
		body = postdata.body
		category=postdata.category
		slug_data=slug.get('slug_data')
		print(image)
		#e = news_posts(title=title, body=body, category=category, slug=slug_data, posted_by='ben',image=image)
		#e.save()
		data['postdata']=postdata


		
		
