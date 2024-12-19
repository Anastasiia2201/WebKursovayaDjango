from django.contrib import admin

from .models import Subject
from teachers.models import TeacherSubject


class TeacherInline(admin.TabularInline):
    model = TeacherSubject
    extra = 0


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    inlines = [TeacherInline,]