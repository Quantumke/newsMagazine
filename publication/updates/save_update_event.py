from publications.model import post_update_event
class SaveUpdateEvent():
	def run (data):
		update_data=data.get('update_data')
		title=update_data.get('title')
		body=update_data.get('body')
		category=update_data.get('category')
		print(title, body, category)
