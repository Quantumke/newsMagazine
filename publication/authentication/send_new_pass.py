from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
class SendNewPass():
	def run(data):
		reset_data=data.get('reset_data')
		email=reset_data.get('email')
		password=reset_data.get('new_password')
		#print(email, password)
		subject = "Your Mup password"
		subject, from_email, to = subject, settings.EMAIL_HOST_USER, email
		text_content = 'Your password has been reset %s' % password
		html_content = "<p>Request to change password was succesful you can now login with""</p>" + str(password)
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.attach_alternative(html_content, "text/html")
		msg.send()
