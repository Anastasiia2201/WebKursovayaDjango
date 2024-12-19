from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('lk/', views.lk , name='lk'),
    path('auth/registration/', views.registration , name='registration'),
    path('auth/login/', views.user_login , name='user_login'),
    path('auth/logout/', views.user_logout , name='user_logout'),
    path('', views.user_login , name='user_login'),
    path('auth/token/', views.token , name='token'),
    path('user/update', views.user_update , name='user_update'),
]