from publication.models import *
class ArchivePost():
	def run(data, id):
		instance= news_post.objects.get(id=id)
		instance.active="not_active"
		print(id)
