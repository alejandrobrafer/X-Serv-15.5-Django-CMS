from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound
from cms.models import Pages


def content(request, key):

	try:
		resource = Pages.objects.get(name=key)
		return HttpResponse(resource.page)
	except Pages.DoesNotExist:
		return HttpResponseNotFound('<h1><center>Resource not found</center></h1>')
