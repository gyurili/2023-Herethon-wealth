from django.shortcuts import render, redirect
from .models import rec_RoutineList, rec_ExerciseList

#Create your views here.
#구현할 거: 추천리스트 함수, 운동리스트 함수(운동명은 html에서 구현하기) 

#루틴 선택 - 첫번째 페이지
def select_routine(request):
    routine_list = rec_RoutineList.objects.all()
    return render(request, 'rec_Routine.html', {'routine_list':routine_list})
#rec_RoutineList 모델에서 모든 객체를 가져오는 쿼리
#해당 루틴을 routine_list에 저장하고, html을 렌더링(routine_list 변수를 템플릿에 전달)

#추천하는 운동 리스트 - 2~4페이지
def exercise_list(request, pk):
    routine = rec_RoutineList.objects.get(pk=pk)
    exercises = rec_ExerciseList.objects.filter(routine=routine)
    exercise1 = exercises[0] 
    exercise2 = exercises[1] 
    exercise3 = exercises[2] 
    exercise4 = exercises[3] 
    exercise5 = exercises[4] 
    exercise6 = exercises[5] 
    exercise7 = exercises[6] 
    return render(request, 'rec_ExerList.html', {'exercise1': exercise1,'exercise2':exercise2, 'exercise3':exercise3,
                                                'exercise4':exercise4, 'exercise5':exercise5, 'exercise6':exercise6, 'exercise7':exercise7})

#주어진 루틴 ID에 해당하는 운동 루틴을 가져오는 쿼리를 사용해 routine에 운동 저장
#가져온 운동들을 exercises에 저장
#html에 렌더링(exercises 변수 전달)

'''

class rec_RoutineList(models.Model):
    content = models.CharField(max_length=30)

    def __str__(self):
        return self.content

#추천 운동 목록 - 운동 이름, 내용(난이도 등) 필요    
class rec_ExerciseList(models.Model):
    routine = models.ForeignKey(rec_RoutineList, on_delete = models.CASCADE)
    name = models.CharField(max_length=25)
    content = models.CharField(max_length=30)

    def __str__(self):
        return self.name
'''

'''
def exercises(request):
    me=request.user.CustomUser()
    new_exercise=Exercises()
    new_exercise.name=request.POST['name']
    new_exercise.save()
    return redirect('home')
    #return render(request, 'rec_Routine.html', {'exercerec_routine':rec_routine})

def home(request):
    return render(request, 'recRoutine/home.html')

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('recRoutine/home.html')

    else:
        form=AuthenticationForm()
        return render(request, 'login.html',{'form':form})
'''
'''
#루틴 추천 리스트
def rec_list(request):
    rec_routine=rec_Routine.objects.all()
    return render(request, 'rec_Routine.html', {'rec_routine':rec_routine})

#저장
def Exercise_list(request):
    Exercise_type_id=request.GET.get('rec_routine_id') #루틴 추천 리스트에서 선택한 옵션 ID
    Exercise_type=rec_Routine.objects.get(id=Exercise_type_id)
    Exerciese=rec_ExerList.objects.filter(exercise_type = Exercise_type)

#home은 아마 존재할 것이므로 todolist 페이지를 url에서 todohome으로 이름 붙여주고 연결

def second_page(request):
    selected_exercise_type_id = request.GET.get('exercise_type_id')
    selected_exercise_type = ExerciseType.objects.get(id=selected_exercise_type_id)
    exercises = Exercise.objects.filter(exercise_type=selected_exercise_type)
    return render(request, 'second_page.html', {'exercises': exercises})

def exercise_list(request):
    exercise_type = request.GET.get('exercise_type')
    exercises = Exercise.objects.filter(exercise_type__name=exercise_type)
    return render(request, 'exercise_list.html', {'exercises': exercises})
    
'''
