from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			messages.success(request, f'Welcome, {username}! Your account is created successfully.')
			return redirect('index')

	else:
		form = UserCreationForm()
	return render(request, 'register.html', {'form' : form})
