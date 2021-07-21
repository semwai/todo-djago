from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='accounts/login')
def index(request):
    return render(request, "index.html")

 
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return HttpResponse("!!")
        else:
            auth_login(request, user)
            return HttpResponseRedirect('/')
            
    else:
        loginform = LoginForm()
        return render(request, "login.html", {"form": loginform} )