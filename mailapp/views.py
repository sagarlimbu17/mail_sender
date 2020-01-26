from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.



def index(request):
    if request.method == 'GET':
        return render(request, "login.html")
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin-dashboard')
        else:
            messages.error(request, messages.ERROR, "Invalid Credentials")
            return render(request, 'login.html')


def send_mail(request):
    return render(request, 'mail-sender.html')
