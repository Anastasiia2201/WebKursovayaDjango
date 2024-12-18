from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from  .models import Teacher


def teachers(request):
    """Отображает страницу пользователя."""
    template = 'teachers/teachers.html'
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, template, context)
