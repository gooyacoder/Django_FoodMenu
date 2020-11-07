from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.

def index(request):
	items = Item.objects.all()
	return render(request, 'index.html', {'items': items,})

def detail(request, item_id):
	return HttpResponse('This is the item no/id: %s' % item_id)
