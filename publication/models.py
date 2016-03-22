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
