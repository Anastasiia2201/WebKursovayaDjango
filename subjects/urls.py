from django.urls import path

from . import views

app_name = 'subjects'

urlpatterns = [
    path('', views.subjects , name='show_subjects'),
]