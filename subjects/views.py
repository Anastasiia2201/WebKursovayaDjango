from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import FileUploadForm
from  subjects.models import Subject,File

@login_required
def subjects(request):
    """Отображает страницу пользователя."""
    template = 'subjects/subjects.html'
    subjects = Subject.objects.all();
    context = {'subjects': subjects}
    return render(request, template, context)


def file_categories(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    categories = ['Лекционные занятия', 'Практические занятия', 'Лабораторные работые', 'Курсовая работа', 'Сессия']
    return render(request, 'subjects/file_categories.html', {'subject': subject, 'categories': categories})


def file_list(request, subject_id, category):
    subject = get_object_or_404(Subject, id=subject_id)
    files = File.objects.filter(subject=subject, category=category)
    return render(request, 'subjects/file_list.html', {'subject': subject, 'category': category, 'files': files})


def upload_file(request, subject_id, category):
    subject = get_object_or_404(Subject, id=subject_id)
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.subject = subject
            file_instance.category = category
            file_instance.save()
    else:
        form = FileUploadForm()
    return render(request, 'subjects/upload_file.html', {'subject': subject, 'category': category, 'form': form})
