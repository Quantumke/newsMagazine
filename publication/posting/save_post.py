from publication.models import news_posts
class SavePost():
	def run (data):
		post_data= data.get('post_data')
		postdata = news_posts(**post_data)
		slug = data.get('slug')
		postdata=news_posts(**post_data)
		title = postdata.title
		body = postdata.body
		category=postdata.category
		slug_data=slug.get('slug_data')
		print(slug_data)
		e = news_posts(title=title, body=body, category=category, slug=slug_data, posted_by='ben')
		e.save()
		data['postdata']=postdata


		
		
