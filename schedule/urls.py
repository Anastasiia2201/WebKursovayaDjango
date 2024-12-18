from django.urls import path

from . import views

app_name = 'schedule'

urlpatterns = [
    path('<str:type>/', views.schedule , name='show_schedule'),
]