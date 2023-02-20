from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from picture.models import Picture
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponse('User logged in')
            else:
                return HttpResponse('invalid credentials')

    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def index(request):
    current_user = request.user
    pictures = Picture.objects.filter(user=current_user)
    return render(request, 'index.html', {'pictures': pictures})

