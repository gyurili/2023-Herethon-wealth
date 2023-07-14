from django.urls import path, include
from . import views

app_name='health'

urlpatterns = [

    # 유새연
    path('', views.main, name='main'),
    path('gym/', views.gym , name='gym'),
    path('gym/reverse/', views.gym_reverse, name='gym_reverse'),
    path('exercise/', views.exercise , name='exercise'),
    path('todo/', views.todo , name='todo'),
    path('gym/like/', views.likeGym, name='likeGym'),
    path('gym/jamaGym/', views.jamaGym , name='jamaGym'),
    path('gym/jamaGym/create', views.create_review , name='create_review'),
    path('gym/jamaGym/update/<int:id>/', views.update_review, name='update_review'),
    path('gym/jamaGym/delete/<int:id>/', views.delete_review, name='delete_review'),
    path('gym/jamaGymevent/', views.jamaGymevent , name='jamaGymevent'),
    path('gym/jamaGymopen/', views.jamaGymopen , name='jamaGymopen'),
    path('gym/jamaGymprice/', views.jamaGymprice , name='jamaGymprice'),
    #박규리
    path('health_list/', views.health_list, name="health_list"),
    path('arm_list/', views.arm_list, name="arm_list"),
    path('overhead/', views.overhead, name="overhead"),
    path('mypage/', views.mypage, name="mypage"),
    path('gym_list/', views.gym_list, name="gym_list"),
    path('exer_list/', views.exer_list, name="exer_list"),
    path('king1/', views.king1, name="king1"),
    path('king2/', views.king2, name="king2"),
    path('king3/', views.king3, name="king3"),
    path('download-photo1/', views.download_photo1, name='download_photo1'),
    path('download-photo2/', views.download_photo2, name='download_photo2'),
    path('download-photo3/', views.download_photo3, name='download_photo3'),
    #
]