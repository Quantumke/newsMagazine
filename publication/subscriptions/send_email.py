from publication.models import *
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
class SendEmail():
	def run(data):
		emails = subscribe.objects.values_list('email', flat=True)
		for email in emails:
			subject = "Our Top Strories"
			subject, from_email, to = subject, settings.EMAIL_HOST_USER, email
			text_content = 'Your'
			html_content = "Yes"
			msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			msg.send()
	
			print(email)
		
