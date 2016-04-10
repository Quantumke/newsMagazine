from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django_mongoengine import Document, EmbeddedDocument, DynamicDocument
from django_mongoengine import fields
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import permalink
import operator



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
class save_user_ip(models.Model):
	ip=models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
	date=models.DateField(default=datetime.now, blank=False)



class news_posts(models.Model):
	title= models.CharField(max_length=200, unique=False)
	body= models.CharField(max_length=1000, unique=False)
	category= models.CharField(max_length=200, unique=True)
	slug= models.SlugField(max_length=200, unique=True)
	active = models.CharField(max_length=100, default='active', blank=False)
	posted_by=models.CharField(max_length=200, unique=False)
	posted_on=models.DateField(default=datetime.now, blank=False)

	def __unicode__(self):
		return '%s' %self.title

	@permalink
	def get_absolute_url(self):
		return('view_more', None, {'slug':self.slug})


class post_transaction(Document):
	title = fields.StringField(max_length=100, unique=False)
	body = fields.StringField(max_length=1000, unique=False)
	category = fields.StringField(max_length=100, unique=True)
	slug= fields.StringField(max_length=100, unique=True)
	posted_by=fields.StringField(max_length=100, unique=False)
	posted_on= fields.DateTimeField(default=datetime.now)


class subscribe(models.Model):
	email=models.CharField(max_length=100, unique=True)
	date=models.DateField(default=datetime.now, blank=False)

	def __unicode__(self):
		return '%s' %self.email

class subscribe_event(Document):
	email=fields.StringField(max_length=100, unique=True)
	date= fields.DateTimeField(default=datetime.now)

class contact_us(models.Model):
	name = models.CharField(max_length=100, unique=False)
	email = models.CharField(max_length=100, unique=False)
	message= models.CharField(max_length=100, unique=False)
	date = models.DateField(default=datetime.now, blank=False)

	def __unicode__(self):
		return '%s'%self.name

class contact_event(Document):
	name= fields.StringField(max_length=100, unique=False)
	email = fields.StringField(max_length=100, unique=False)
	message=fields.StringField(max_length=100, unique=False)
	date= fields.DateTimeField(default= datetime.now, )


class post_update_event(Document):
	title= fields.StringField(max_length=100, unique=False)
	body = fields.StringField(max_length=1000 , unique=False)
	category=fields.StringField(max_length=100, unique=False)
	date=fields.DateTimeField(default=datetime.now)


class savearchiveevent(Document):
	title= fields.StringField(max_length=100, unique=False)
	body = fields.StringField(max_length=1000, unique=False)
	category = fields.StringField(max_length=100, unique=False)
	date=fields.DateTimeField(default=datetime.now)

class forgotpassword(models.Model):
	email= models.CharField(max_length=100, unique=False)
	password=models.CharField(max_length=100, unique=False)

class reset_password(models.Model):
	email=models.CharField(max_length=100, unique=False)
	password=models.CharField(max_length=100, unique=False)
	new_password=models.CharField(max_length=100, unique=False)