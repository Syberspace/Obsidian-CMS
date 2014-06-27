from guestbook.models import GuestbookEntry
from guestbook.models import GuestbookEntryForm
from pages.models import Page
from config.models import SiteConfig, ImprintConfig
from django.template import Context, loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.context_processors import csrf

def entries(request):
    entries = GuestbookEntry.objects.all().order_by('date', 'time').reverse()
    list_pages = Page.objects.all().order_by('order')
    confS = SiteConfig.objects.get()          
    confI = ImprintConfig.objects.get()
        
    t = loader.get_template('guestbook/entries.html')
    c = Context({
        'entries':entries,
        'list_pages':list_pages,
        'site_config':confS,
        'imprint_config':confI,
    })
    return HttpResponse(t.render(c))

def addEntry(request):
	if request.method == 'POST':
		form = GuestbookEntryForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('.')
		
	else:
		form = GuestbookEntryForm()
	
	list_pages = Page.objects.all().order_by('order')
	confS = SiteConfig.objects.get()          
	confI = ImprintConfig.objects.get()
        
	t = loader.get_template('guestbook/addEntry.html')
	c = Context({
		'form':form,
		'list_pages':list_pages,
		'site_config':confS,
		'imprint_config':confI,
	})
	c.update(csrf(request))
	return HttpResponse(t.render(c))
    