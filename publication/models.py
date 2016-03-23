from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django_mongoengine import Document, EmbeddedDocument, DynamicDocument
from django_mongoengine import fields
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import permalink


# Create your models here

class auth_user(models.Model):
	user= models.OneToOneField(User)
	
	def __unicode__(self):
		return self.user.username

class save_registration_transaction(DynamicDocument):
	 username = fields.StringField(max_length=200, required=True)
	 email = fields.StringField(max_length=200, required=True)
	 password= fields.StringField(max_length=200, required=True)
	 firstname= fields.StringField(max_length=200, required=True)
	 lastname= fields.StringField(max_length=200, required=True)

