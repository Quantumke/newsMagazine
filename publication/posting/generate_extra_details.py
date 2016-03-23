import uuid
class GenerateExtraDetails():
	def run(request_data, data):
		data['generate_slug']=GenerateExtraDetails.generate_slug(request_data)
	
	def generate_slug(request_data):
		slug ={}
		slug['slug']= uuid.uuid4()

	