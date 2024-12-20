from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Teacher, TeacherSubject

@login_required
def teachers(request):
    """Отображает страницу пользователя."""
    template = 'teachers/teachers.html'
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, template, context)


def teacher_subjects(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)  # Находим преподавателя по ID
    teacher_subjects = TeacherSubject.objects.filter(teacher=teacher)  # Получаем все записи для этого преподавателя
    subjects = [ts.subject for ts in teacher_subjects]  # Извлекаем все предметы для данного преподавателя
    context = {'teacher': teacher, 'subjects': subjects}
    return render(request, 'teachers/teacher_subjects.html', context)


