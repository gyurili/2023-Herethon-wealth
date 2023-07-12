from django.contrib import admin
from django.urls import path, include
from health import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('health.urls'), name='health'),
    path('search/', include('search_app.urls')),
]
