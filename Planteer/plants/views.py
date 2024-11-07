from django.shortcuts import render, redirect , get_object_or_404
from django.http import Http404
from django.http import HttpRequest
from .models import Plant, Country
from django.http import JsonResponse


def add_plant_view(request: HttpRequest):
    if request.method == "POST":
        title = request.POST.get('title')
        about = request.POST.get('about')
        used_for = request.POST.get('used_for')
        category = request.POST.get('category')  
        is_edible = request.POST.get('is_edible') == 'True' 
        image = request.FILES.get('image')
        native_to = request.POST.getlist('native_to')

        
        plant = Plant.objects.create(
            title=title,
            about=about,
            used_for=used_for,
            category=category,  
            is_edible=is_edible,
            image=image,
        )

      
        for country_id in native_to:
            country = Country.objects.get(id=country_id)
            plant.native_to.add(country)

       
        return redirect('plants:all_plants_view')

   
    categories = Plant.Category.choices  
    countries = Country.objects.all()
    return render(request, 'plants/add_plant.html', {
        'categories': categories,
        'countries': countries,
    })


def all_plants_view(request):
    plants = Plant.objects.all()
    return render(request, 'plants/all_plants.html', {'plants': plants})

def plant_detail_view(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    return render(request, 'plants/plant_detail.html', {'plant': plant})

def delete_plant_view(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    
    if request.method == 'POST':
        plant.delete()
        return redirect('plants:all_plants_view')  
    
    return render(request, 'plants/delete.html', {'plant': plant})

'''
def search_countries(request):
    query = request.GET.get('query', '')
    countries = Country.objects.filter(name__icontains=query).values('id', 'name')[:10] 
    return JsonResponse(list(countries), safe=False)

'''