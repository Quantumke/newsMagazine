from publication.models import *
class SaveUpdate():
	def run(data, id):
		instance = news_posts.objects.get(id=id)
		update_data=data.get('update_data')
		instance.title=update_data.get('title')
		instance.body=update_data.get('body')
		instance.category=update_data.get('category')
		instance.save()
		#print(title,instance.category, instance.body)
