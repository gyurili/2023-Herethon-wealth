from django.contrib import admin
from django.urls import path, include

import account.views
import todo.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('health.urls')),
    path('search/', include('search_app.urls')),
    
    path('account/login', account.views.login_view, name = "login"),
    path('account/logout', account.views.logout_view, name = "logout"),
    path('account/signup', account.views.signup_view, name="signup"),
    path("todolists/",todo.views.todolist, name="todohome"),
    path("create/",todo.views.create, name="create"),
    path("delete/<int:todo_id>",todo.views.delete, name="delete"),
    path("update/<int:todo_id>",todo.views.update, name="update"),
]
