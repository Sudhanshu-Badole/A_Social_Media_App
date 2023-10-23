from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
# Create your views here.
def user_login(request):
    if request.method == 'POSt':
        form = LoginForm(request.POST)
        if form.is_vaild():
            data = form.cleaned_data
            user = authenticate(request, username = data['username'], password = data['password'])
            if user is not None:
                login(request, user)
                return HttpResponse('User Logged In')
            else:
                return HttpResponse('Invail Login')
    else:
        form = LoginForm()

        return render(request, 'users/login.html', {'form':form})