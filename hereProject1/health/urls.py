from django.contrib import admin
from django.urls import path
from health import views

urlpatterns = [
    path('', views.home, name='main'),
    path('gym/', views.gym , name='gym'),
    path('exercise/', views.exercise , name='exercise'),
    path('todo/', views.todo , name='todo'),
    path('mypage/', views.mypage, name='mypage'),
    path('gym/like/', views.likeGym, name='likeGym'),
    path('gym/jamaGym/', views.jamaGym , name='jamaGym'),
]
