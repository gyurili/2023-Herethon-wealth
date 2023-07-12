from django.shortcuts import render, redirect
from .models import gymPlace, gymReview
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.
# urls.py 에 연결시키기 위해 임의 함수 작성 -> 
# 나중에 함수명 변경하거나, 프로젝트 urls.py 주소 변경

def home(request):
    return render(request, "main.html")

def exercise(request):
    return render(request, "exercise.html")

def todo(request):
    return render(request, "todo.html")

def mypage(request):
    return render(request, "mypage.html")

def jamaGym(request):
    # 헬스장 리뷰
    reviews = gymReview.objects.all()
    return render(request, 'jamaGym.html', {'reviews': reviews})

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