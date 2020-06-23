from django.http import HttpResponse
from django.template import Template, Context

def main_page(request):

	'''This is the main view for the personal web. Its
	asociated to the template located in structure/index.html

	The htm document is saved in a variable called 'doc'
	and after that it's charged in a Template object called ptx. The context
	is created in a Context object and html is the final view, the ptx object
	after calling the .render() method with ctx as argument.'''

	doc = open('C:/Users/sedwi/Desktop/Programas/python/django/personal_website/personal_website/structure/index.html')

	ptx = Template(doc.read())

	doc.close()

	ctx = Context()

	html = ptx.render(ctx)
	
	return HttpResponse(html)