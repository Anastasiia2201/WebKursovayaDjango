from django.urls import path

from . import views

app_name = 'teachers'

urlpatterns = [
    path('', views.teachers , name='show_teachers'),
    path('<int:teacher_id>/subjects/', views.teacher_subjects, name='teacher_subjects'),
]