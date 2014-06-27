from django.db import models
from django.contrib import auth

class Page(models.Model):
    content = models.TextField(help_text="You can use html-code here")
    short_name = models.CharField(max_length=255)
    display_name=models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published', auto_now=True, auto_now_add=True)
    author = models.ForeignKey(auth.models.User)
    order = models.IntegerField()
    flag_public = models.BooleanField('public')
 
    
    def __unicode__(self):
        return self.content