from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm



def index(request):
	items = Item.objects.all()
	return render(request, 'index.html', {'items': items,})

def details(request, item_id):
	item = Item.objects.get(pk=item_id)
	context = { 'item' : item }
	return render(request, 'details.html', context)

def create_item(request):
	form = ItemForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('index')

	return render(request, 'item_form.html', {'form': form})
