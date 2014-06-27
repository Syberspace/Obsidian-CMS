from pages.models import Page
from django.contrib import admin

class PageAdmin(admin.ModelAdmin):
    fieldsets=[
        ('Navigation', {'fields':['short_name', 'display_name']}),
        (None, {'fields':['content']}),
        ('Management', {'fields':['author','flag_public', 'order']}),
    ]
    list_display=['short_name','display_name', 'pub_date','author', 'flag_public', 'order']
    ordering=['order']
    class Media:
        js = (
                '/static/tiny_mce/tiny_mce.js',
                '/static/textareas.js',
            )
            
    def has_delete_permission(self, request, obj=None):
        if obj and obj.short_name == 'home':
            return False
        return True

admin.site.register(Page,PageAdmin)