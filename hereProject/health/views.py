from health.models import *
from account.models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, FileResponse
import os
from django.conf import settings
from django.db.models import Q
from django.http import JsonResponse
from .forms import PostModelForm
from django.contrib.auth import get_user_model

# Create your views here. (↓박규리)

#전체 운동 목록
def health_list(request):
    healths = Health.objects.all()
    context = {
        "healths" : healths,
    }
    return render(request, "health_list.html", context)

#어깨&팔 운동 목록
def arm_list(request):
        keyword = request.GET.get('keyword')      
        categories = Category.objects.all()
        if keyword is not None:   
                aHealths = Arm_Health.objects.filter(arm_name__contains=keyword)
                context = {
                    "categories": categories,
                    "aHealths": aHealths,
                }
                return render(request, 'arm_list.html', context)
        else:
                aHealths = Arm_Health.objects.all()
                context = {
                    "categories": categories,
                    "aHealths": aHealths,
                }
                return render(request, 'arm_list.html', context)

#오버헤드 익스텐션
def overhead(request):
    return render(request, "overhead.html")

#마이페이지
def mypage(request):
    customUser = CustomUser.objects.all()
    context = {
                    "customUser": customUser
                }
    return render(request, "mypage.html", context)

#찜한 헬스장 목록
def gym_list(request):
    likes = Gym_list.objects.all()
    context = {
                    "likes": likes
                }
    return render(request, "gym_list.html", context)

#스크랩한 운동 목록
def exer_list(request):
    likes = Exer_list.objects.all()
    context = {
                    "likes": likes
                }
    return render(request, "exer_list.html", context)

#성실왕
def king1(request):
    return render(request, "king1.html")
def download_photo1(request):
    file_path = os.path.join(settings.BASE_DIR, 'static/img/성실왕.jpg')
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename="성실왕.jpg"'
    return response

#운동왕
def king2(request):
    return render(request, "king2.html")
def download_photo2(request):
    file_path = os.path.join(settings.BASE_DIR, 'static/img/운동왕.jpg')
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename="운동왕.jpg"'
    return response

#끈기왕
def king3(request):
    return render(request, "king3.html")
def download_photo3(request):
    file_path = os.path.join(settings.BASE_DIR, 'static/img/끈기왕.jpg')
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename="끈기왕.jpg"'
    return response

# Create your views here. (↓유새연)
# urls.py 에 연결시키기 위해 임의 함수 작성 -> 
# 나중에 함수명 변경하거나, 프로젝트 urls.py 주소 변경

def main(request):
    return render(request, "main.html")

def exercise(request):
    return render(request, "exercise.html")

def todo(request):
    return render(request, "todo.html")

def jamaGym(request):
    # 헬스장 리뷰
    reviews = gymReview.objects.all()
    return render(request, 'jamaGym.html', {'reviews': reviews})

def jamaGymevent(request):
    # 헬스장 리뷰
    reviews = gymReview.objects.all()
    return render(request, 'jamaGymevent.html', {'reviews': reviews})

def jamaGymopen(request):
    # 헬스장 리뷰
    reviews = gymReview.objects.all()
    return render(request, 'jamaGymopen.html', {'reviews': reviews})

def jamaGymprice(request):
    # 헬스장 리뷰
    reviews = gymReview.objects.all()
    return render(request, 'jamaGymprice.html', {'reviews': reviews})

def gym(request):
    places = gymPlace.objects.all()
    return render(request, 'gym.html', {'places': places})


# 좋아요
def likeGym(request):
    if request.method == 'POST':
        place_id = request.POST.get('place_id')
        user = request.user

        try:
            place = gymPlace.objects.get(id=place_id)
        except gymPlace.DoesNotExist:
            return JsonResponse({'success': False})

        if user in place.likes.all():
            place.likes.remove(user)
            liked = False
        else:
            place.likes.add(user)
            liked = True

        return JsonResponse({'success': True, 'liked': liked})
    else:
        return JsonResponse({'success': False})
    
def gym_reverse(request):
    places = reversed(gymPlace.objects.all())
    return render(request, 'gym.html', {'places': places})

def create_review(request):
    if request.method == 'POST':
        # 입력 내용을 DB에 저장
        form = PostModelForm(request.POST)
        # 제대로 입력되었는지 검사하는 코드
        if form.is_valid(): 
            # 유효하다면 저장하는 코드
            form.save() 
            return redirect('health:jamaGym') 
    else:
        form = PostModelForm() 
    return render(request, 'form_create.html', {'form':form})

def update_review(request):
    post = get_object_or_404(gymPlace, pk=id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('health:jamaGym')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'form_create.html', {'form':form, 'id':id})

def delete_review(request, id):
    post = gymPlace.objects.get(pk=id)
    post.delete()
    return redirect('health:jamaGym')