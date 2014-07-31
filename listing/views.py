from django.shortcuts import render, render_to_response
from django.template import RequestContext
# Create your views here.
from django.http import HttpResponse
from listing.models import Product
from django.http import HttpResponseNotFound  


def index(request):
	context=RequestContext(request)
	product_list=Product.objects.order_by('-time')[:10]
	context_dict={'products':product_list}
	for product in product_list:
		product.url = product.id
	return render_to_response('listing/index.html',context_dict,context)

def products_page(request,product_name_url):

	context = RequestContext(request)
	# product_name=product_name_url.replace('_',' ')
	context_dict={'product_url':product_name_url}
	try:
		product=Product.objects.get(id=product_name_url)
		
		context_dict['product']=product
	except Product.DoesNotExist:
		return HttpResponseNotFound('<h1>404 you are lost No Page Here</h1>') 
		pass
	return render_to_response('listing/product.html',context_dict,context)