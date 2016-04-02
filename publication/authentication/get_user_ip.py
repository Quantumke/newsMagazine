from socket import gethostname, gethostbyname
from publication.models import *
import httpagentparser
class GetUserIp():
	def run(data, request):
		ip=gethostbyname(gethostname())
		ip=ip
		save=save_user_ip(ip=ip)
		save.save()
		print(ip)
		
