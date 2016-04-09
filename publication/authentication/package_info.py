from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives


class PackageInfo():
	def run(data):
		email=data.get('email')
		password=data.get('password')
		#print(email, password)

		subject ="Your Mup password"
		subject, from_email, to = subject, settings.EMAIL_HOST_USER, email
		text_content = 'You requested your password %s' % password
		html_content = "<p>Password Reset succesful""</p>"+str(password)
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.attach_alternative(html_content, "text/html")
		msg.send()

