from django.urls import path
from . import views

#app_name = "account"

urlpatterns = [
    path('', views.poppage, name='poppage'),
    path('face/', views.face, name='face'),
    path('login1/', views.login1, name='login1'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('logout/', views.logout_view, name='logout_view'),
]