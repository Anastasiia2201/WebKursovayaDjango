from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from  subjects.models import Subject

@login_required
def subjects(request):
    """Отображает страницу пользователя."""
    template = 'subjects/subjects.html'
    subjects = Subject.objects.all();
    context = {'subjects': subjects}
    return render(request, template, context)
