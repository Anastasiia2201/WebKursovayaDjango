from django.contrib import admin

from .models import Teacher, TeacherSubject


class SubjecttInline(admin.TabularInline):
    model = TeacherSubject
    extra = 0


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [SubjecttInline,]