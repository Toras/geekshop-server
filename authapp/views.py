from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import UserLoginForm, UserRegisterForm
from django.contrib import auth, messages
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(redirect_to=reverse('index'))
    else:
        form = UserLoginForm()
    context = {'title': 'GeekShop - Авторизация', 'form': form}
    return render(request, 'authapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация пользователя прошла успешно!')
            return HttpResponseRedirect(redirect_to=reverse('users:login'))
    else:
        form = UserRegisterForm()
    context = {'title': 'GeekShop - Регистрация', 'form': form}
    return render(request, 'authapp/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(redirect_to=reverse('index'))
