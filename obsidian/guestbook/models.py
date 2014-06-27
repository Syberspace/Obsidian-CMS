from django.db import models
from django.forms import ModelForm

class GuestbookEntry(models.Model):
	nickname = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	flag_showmail = models.BooleanField('Show eMail')
	text = models.TextField()
	time = models.TimeField(auto_now=True)
	date = models.DateField(auto_now=True)
    
	def __unicode__(self):
		return self.nickname + " | " + self.email
		
class GuestbookEntryForm(ModelForm):
	class Meta:
		model = GuestbookEntry