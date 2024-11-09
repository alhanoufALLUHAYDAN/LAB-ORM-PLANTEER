from django.shortcuts import render
from django.http import HttpRequest
from plants.models import Plant

def home_view(request: HttpRequest):
    return render(request, 'main/home.html')

def search_results(request: HttpRequest):
    query = request.GET.get('query', '')
    if query:
        results = Plant.objects.filter(
            title__icontains=query
        ) | Plant.objects.filter(
            about__icontains=query
        ) | Plant.objects.filter(
            used_for__icontains=query
        ) | Plant.objects.filter(
            category__icontains=query
        )
    else:
        results = Plant.objects.none()
    return render(request, 'main/results.html', {'results': results, 'query': query})
