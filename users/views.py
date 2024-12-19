from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password

from users.forms import RegistrationForm, LoginForm, TokenForm, UpdateForm

User = get_user_model()

@login_required
def lk(request):
    """Отображает страницу пользователя."""
    template = 'users/lk.html'
    user = get_object_or_404(User, id=1)
    print(user.get_role_display() )
    context = {'profile': user}
    return render(request, template, context)

def registration(request):
    template = 'users/registration.html'
    form = RegistrationForm(
        request.POST or None,
        files=request.FILES or None,)
    context = {'form': form}
    if form.is_valid():
        user = form.save()
        return redirect('schedule:show_schedule', type='today')
    return render(request, template, context)

def user_login(request):
    if request.user.is_authenticated:
         return redirect('schedule:show_schedule', type='today')
    template = 'users/login.html'
    form = LoginForm(
        request.POST or None,
        files=request.FILES or None,)
    context = {'form': form}
    if request.method == 'POST':
        user = User.objects.filter(email=form.data['email']).first()
        if user and user.check_password(form.data['password']):
            login(request, user)
            return redirect('schedule:show_schedule', type='today')
        else:
            context.update({'error': "Неверный email или пароль"}) 
    return render(request, template, context)

def token(request):
    template = 'users/token.html'
    form = TokenForm(
        request.POST or None,
        files=request.FILES or None,)
    context = {'form': form}
    if request.method == 'POST':
        user = User.objects.filter(email=form.data['email']).first()
        token = form.data['token']
        if user and default_token_generator.check_token(user, token):
            login(request, user)
            print(5)
            return redirect('users:user_update')
        else:
            context.update({'error': "Неверный email или токен"}) 
    return render(request, template, context)

@login_required
def user_logout(request):
    logout(request) 
    return redirect('users:user_login')

@login_required
def user_update(request):
    template = 'users/update.html'
    user = request.user
    print(user)
    form = UpdateForm(request.POST or None,instance=user,files=request.FILES or None)
    context = {'form': form}
    if request.method == 'POST' and form.is_valid():
        hashed_pwd = make_password(form.cleaned_data['password'])
        user = form.save(commit=False)
        user.password = hashed_pwd
        user.save()
        login(request, user)
        return redirect('users:lk')
    else:
        print()
    return render(request, template, context)
