from django.urls import path

from . import views

app_name = 'subjects'

urlpatterns = [
    path('', views.subjects , name='show_subjects'),
    path('<int:subject_id>/files/', views.file_categories, name='file_categories'),
    path('<int:subject_id>/files/<str:category>/', views.file_list, name='file_list'),
    path('<int:subject_id>/files/<str:category>/upload/', views.upload_file, name='upload_file'),
]