import uuid
class GenerateExtraDetails():
	def run(request_data, data):
		data['slug']=GenerateExtraDetails.generate_slug(request_data)
	
	def generate_slug(request_data):
		slug ={}
		random = str(uuid.uuid4())
		random = random.upper()
		random = random.replace("-", "")
		random =  ''.join([i for i in random if not i.isdigit()])
		slug['slug_data']= random
		# print(slug)
		return slug

	