from django.db import models
from django.core.exceptions import ValidationError
        
class SiteConfig(models.Model):
	site_admin = models.CharField(max_length=255)
	site_admin_email = models.CharField(max_length=255)
	site_name = models.CharField(max_length=255)
	site_header = models.TextField(max_length=255, help_text="The Headimage for the site. (e.g. /img/header.png) The Picture needs to be placed in the /static/ directory")
    
	def __unicode__(self):
		return self.site_admin + " | " + self.site_admin_email + " | " + self.site_name + " | " + self.site_header   
        

class ImprintConfig(models.Model):
	address = models.CharField(max_length=500)
	zipcode = models.CharField('ZIP/Postal-Code', max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField('State/Province', max_length=255)
	country = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	flag_visible = models.BooleanField('visible')
	
	def __unicode__(self):
		return self.address + " | " + self.zipcode + " | " + self.city + " | " + self.state + " | " + self.country + " | " + self.phone       