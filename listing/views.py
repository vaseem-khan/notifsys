from django.shortcuts import render, render_to_response
from django.template import RequestContext
# Create your views here.
from django.http import HttpResponse
from listing.models import Product
def index(request):
	context=RequestContext(request)
	product_list=Product.objects.order_by('-time')[:5]
	context_dict={'products':product_list}
	return render_to_response('listing/index.html',context_dict,context)