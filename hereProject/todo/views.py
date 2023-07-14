from django.shortcuts import render, redirect, get_object_or_404
from .models import *

#Create your views here.

#투두리스트 메인화면
def todolist(request):
    todos=Todo.objects.filter(is_done=False) #필터링
    dones=Todo.objects.filter(is_done=True)
    return render(request, 'todohome.html', {'todos':todos,'dones':dones})
#home.html 없어서 에러. 프엔 home 역할 하는 부분으로 바꿔주기

#저장
def create(request):
    new_todo=Todo()
    new_todo.content=request.POST['content']
    new_todo.is_done=False
    new_todo.save()
    return redirect('todohome')
#home은 아마 존재할 것이므로 todolist 페이지를 url에서 todohome으로 이름 붙여주고 연결

def delete(request, todo_id):
    todo_delete=get_object_or_404(Todo,pk=todo_id)
    todo_delete.delete()
    return redirect('todohome')

#완료여부 변경
def update(request, todo_id):
    todo_update=get_object_or_404(Todo, pk=todo_id)
    if todo_update.is_done==True:
        todo_update.is_done=False
    else:
        todo_update.is_done=True
    todo_update.save()
    return redirect('todohome')


#오늘의운동 완료하기 넣어야함