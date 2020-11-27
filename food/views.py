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

def update_item(request, id):
	item = Item.objects.get(id=id)
	form = ItemForm(request.POST or None, instance=item)

	if form.is_valid():
		form.save()
		return redirect('index')

	return render(request, 'item_form.html', {'form': form, 'item': item})

def delete_item(request, id):
	item = Item.objects.get(id=id)

	if request.method == 'POST':
		item.delete()
		return redirect('index')

	return render(request, 'item_delete.html', {'item': item})