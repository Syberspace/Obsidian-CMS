from config.models import SiteConfig, ImprintConfig
from django.contrib import admin

#class ConfigAdmin(admin.ModelAdmin):
#    fields=['config_name', 'config_description', 'config_value']
#    list_display=['config_name', 'config_description']
    
class SiteConfigAdmin(admin.ModelAdmin):
    fields=['site_admin', 'site_admin_email', 'site_name', 'site_header']
    
    def has_add_permission(self, request):
        return False
        
    def has_delete_permission(self, request, obj=None):
        return False
        
        
class ImprintConfigAdmin(admin.ModelAdmin):
    fields=['address', 'zipcode','city', 'state', 'country', 'phone', 'flag_visible']
    change_list_template = 'admin/Config/ImprintConfig/change_list.html'
    def has_add_permission(self, request):
        return False
        
    def has_delete_permission(self, request, obj=None):
        return False
        

admin.site.register(SiteConfig,SiteConfigAdmin)
admin.site.register(ImprintConfig,ImprintConfigAdmin)