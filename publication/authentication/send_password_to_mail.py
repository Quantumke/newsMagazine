from publication.models import *
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

class SendPasswordToMail():
	def run(data):
		user_data=data.get('user_data')
		new_user= User(**user_data)
		password=(data.get('random_password'))
		email = user_data.get('email')
		username= user_data.get('username')
		# print(password, email)
		subject ="Your Mup password"
		subject, from_email, to = subject, settings.EMAIL_HOST_USER, email
		text_content = 'Thank you for registering %s' % password
		html_content = "<p>Thank you for registering, you can now login to MUP with the password""</p>"+str(password)
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.attach_alternative(html_content, "text/html")
		msg.send()

				