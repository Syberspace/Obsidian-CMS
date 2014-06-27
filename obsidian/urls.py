from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pages.views.index'),
    #url(r'^admin/', 'django.contrib.staticfiles'), 
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/config/imprintconfig$', 'config.admin_views.report'),
    # url(r'^obsidian/', include('obsidian.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^page/imprint/', 'config.views.imprint'),
	
	url(r'^page/guestbook/new', 'guestbook.views.addEntry'),
    url(r'^page/guestbook/', 'guestbook.views.entries'),
	
    url(r'^page/(?P<short_name>\w+)/$', 'pages.views.page'), #all normal pages, must be last
)
urlpatterns += staticfiles_urlpatterns()
