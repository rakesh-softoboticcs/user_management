from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Users
from django.contrib.auth import authenticate, login, logout


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Users.objects.get(user_name=username)

        except:
            messages.error(request, 'User does not exist')

        user = Users.objects.filter(user_name=username, password=password)
        global_username = username
        global_password = password

        if user:
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    context = {'page': page}
    return render(request, 'login.html', context)


# @login_required(login_url='login', redirect_field_name='home')
def home(request):
    values = Users.objects.all()
    print(values)
    context = {'values': values}
    return render(request, 'home.html', context)


def register(request):
    forms = UserForm()
    if request.method == 'POST':
        print('request.POST: ', request.POST)
        forms = UserForm(request.POST)
        if forms.is_valid():
            print('is valid')
            forms.save()
            forms = UserForm()
            return redirect('home')

    context = {'forms': forms}
    return render(request, 'register.html', context)


def edit(request, id):
    user = Users.objects.get(id=id)
    forms = UserForm(instance=user)
    if request.method == 'POST':
        forms = UserForm(request.POST, instance=user)
        if forms.is_valid():
            forms.save()
            return redirect('home')

    context = {'forms': forms}
    return render(request, 'edit.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')


def delete(request, id):
    user = Users.objects.get(id=id)
    user.delete()
    users = Users.objects.all()
    return redirect('home')
