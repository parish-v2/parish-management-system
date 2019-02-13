from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.views.generic.list import ListView
from django.contrib.auth.models import User


# Create your views here.

@login_required
def index(request):
	return render(request, 'registration/index.html')

def register(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('registration-index')
	else:
		form = SignUpForm()
	return render(request, 'registration/register.html', {'form': form})


class UserListView(ListView):
	model = User
	template_name = 'registration/user_list.html'
	ordering = ['-date_joined']