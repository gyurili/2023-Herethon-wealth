from django.urls import path
from . import views

app_name='todo'

urlpatterns = [
    path('',views.todolist, name="todohome"),
    path('create/',views.create, name="create"),
    path('delete/<int:todo_id>',views.delete, name="delete"),
    path('update/<int:todo_id>',views.update, name="update"),
    path('add/',views.add_todo, name='add_todo'),
    path('todolist/',views.todolist, name="todolist"),
    #path('wish/',views.wish, name="wish"),
    #path('routine/',views.routine, name="routine"),
    
]
