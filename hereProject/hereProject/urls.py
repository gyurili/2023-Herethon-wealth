from django.contrib import admin
from django.urls import path, include
from account.views import *
from todo.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('health/', include('health.urls')),
    path('search/', include('search_app.urls')),
    path('account/', include('account.urls')),
    path('todolists/', include('todo.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)