from publication.models import *
class DeletePost():
	def run(data, id):
		instance = news_posts.objects.get(id=id)
		instance.active="not_active"
		instance.save()
		#print(id)
		
