from publication.models import *
class SaveArchiveEvent():
	def run(data, id):
		instance = news_posts.objects.get(id=id)
		title = instance.title
		body= instance.body
		category= instance.category
		save=savearchiveevent(title=title, body=body,category=category)
		save.save()
		#print(title, body, category)

