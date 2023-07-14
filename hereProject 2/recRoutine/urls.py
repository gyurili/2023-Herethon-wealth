from django.urls import path
from . import views

app_name='recRoutine'

urlpatterns = [
    path('', views.select_routine, name='select_routine'),
    path('exercise_list/<int:pk>', views.exercise_list, name='exercise_list'),
    # path('list/<int:pk>', views.exercise_list, name='exercises'),

]
