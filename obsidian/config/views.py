from pages.models import Page
from config.models import SiteConfig, ImprintConfig
from django.template import Context, loader
from django.http import HttpResponse, Http404

def imprint(request):
	try:
		list_pages = Page.objects.all().order_by('order')
		confS = SiteConfig.objects.get()          
		confI = ImprintConfig.objects.get()

	except Page.DoesNotExist:  
		raise Http404

	t = loader.get_template('pages/imprint.html')
	c = Context({
		'list_pages':list_pages,
		'site_config':confS,
		'imprint_config':confI,
	})
	return HttpResponse(t.render(c))
