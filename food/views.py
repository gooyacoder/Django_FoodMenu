from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.

def index(request):
	return HttpResponse(Item.objects.all())
