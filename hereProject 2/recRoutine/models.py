from django.db import models
from django.contrib.auth.models import User
from todo.models import Todo

# Create your models here.
#class - 추천루틴 항목, 세부 운동 항목 + 선택항목 저장하는 class(루틴 선택해서 todo로 넘기게)

#추천 루틴 항목 - 루틴 내용(ex-근력운동이 처음이에요) 필요
class rec_RoutineList(models.Model):
    content = models.CharField(max_length=30)

    def __str__(self):
        return self.content

#추천 운동 목록 - 운동 이름, 내용(난이도 등) 필요    
class rec_ExerciseList(models.Model):
    routine = models.ForeignKey(rec_RoutineList, on_delete = models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    content = models.CharField(max_length=30)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='exercises', null=True, blank=True, default=1)

    def __str__(self):
        return self.name
