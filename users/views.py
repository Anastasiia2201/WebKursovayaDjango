from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from  users.models import User


def lk(request):
    """Отображает страницу пользователя."""
    template = 'users/lk.html'
    user = get_object_or_404(User, id=1)
    print(user.get_role_display() )
    context = {'profile': user}
    return render(request, template, context)
