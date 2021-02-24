from django.shortcuts import render, redirect
from .models import UserModel
from .forms import UserForm

# Create your views here.


def signupfunc(request):
    return render(request, 'signup.html')

def loginfunc(request):
    return render(request, 'login.html')

def logoutfunc(request):
    return redirect('welcome')

def homefunc(request):
    #username = request.user.get_username()
    #context = {'username':username}
    user = UserModel.objects.all()
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home.html')
    context = {'user':user, 'form':form}
    return render(request, 'home.html', context)

def createfunc(request):
    user = UserModel.objects.all()
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home.html')
    context = {'user':user, 'form':form}
    return render(request, 'home.html', context)