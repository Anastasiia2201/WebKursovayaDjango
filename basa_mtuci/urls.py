from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls', namespace='users')),
    path('schedule/', include('schedule.urls', namespace='schedule')),
    path('subjects/', include('subjects.urls', namespace='subjects')),
    path('teachers/', include('teachers.urls', namespace='teachers')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)