from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.

def index(request):
	items = Item.objects.all()
	return render(request, 'index.html', {'items': items,})

def details(request, item_id):
	item = Item.objects.get(pk=item_id)
	context = { 'item' : item }
	return render(request, 'details.html', context)
