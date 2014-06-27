from guestbook.models import GuestbookEntry
from django.contrib import admin

class GuestbookAdmin(admin.ModelAdmin):
    fields=['nickname', 'email', 'flag_showmail', 'text']
    list_display=['nickname','email', 'flag_showmail', 'text']
	
admin.site.register(GuestbookEntry,GuestbookAdmin)
