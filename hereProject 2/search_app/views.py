from django.shortcuts import render
from health.models import gymPlace
from django.db.models import Q

# Create your views here.
def searchResult(request):
    places = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        places = gymPlace.objects.all().filter(Q(placeName__contains=query) | Q(created_at__contains=query))

    return render(request, 'search.html', {'query': query, 'places': places})
