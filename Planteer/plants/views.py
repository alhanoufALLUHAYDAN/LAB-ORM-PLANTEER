from django.shortcuts import render, redirect , get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpRequest
from .models import Plant, Country
from django.contrib import messages
import random
from django.db.models import Q



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
    category = request.GET.get('category')
    is_edible = request.GET.get('is_edible')
    if category:
        plants = plants.filter(category=category)
    if is_edible:
        plants = plants.filter(is_edible=(is_edible == 'True'))
    
    paginator = Paginator(plants, 3)
    page_number = request.GET.get('page')
    plants = paginator.get_page(page_number)
    
    categories = Plant.Category.choices
    return render(request, 'plants/all_plants.html', {
        'plants': plants,
        'categories': categories,
    })


def plant_detail_view(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    related_plants = list(Plant.objects.filter(category=plant.category).exclude(id=plant.id))
    random.shuffle(related_plants) 
    countries = Country.objects.all()
    categories = Plant.Category.choices
    
    return render(request, 'plants/plant_detail.html', {
        'plant': plant,
        'related_plants': related_plants[:5], 
        'countries': countries,
        'categories': categories,
    })


def delete_plant_view(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    
    if request.method == 'POST':
        plant.delete()
        return redirect('plants:all_plants_view')  
    

def update_plant_view(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    countries = Country.objects.all()
    categories = Plant.Category.choices

    if request.method == 'POST':
        plant.title = request.POST.get('title')
        if not plant.title: 
            return redirect('plants:update_plant_view', plant_id=plant.id)
        plant.about = request.POST.get('about')
        plant.used_for = request.POST.get('used_for')
        plant.is_edible = request.POST.get('is_edible') == 'True'
        plant.category = request.POST.get('category')

        if 'image' in request.FILES:
            plant.image = request.FILES['image']

        native_to_ids = request.POST.getlist('native_to')
        plant.native_to.set(native_to_ids)

        plant.save()

        messages.success(request, 'Plant updated successfully')
        return redirect('plants:plant_detail_view', plant_id=plant.id)

    return render(request, 'plants/update_plant.html', {
        'plant': plant,
        'countries': countries,
        'categories': categories,
    })



def search_plants_view(request):
    search_title = request.GET.get('query', '').strip()
    
    plants = Plant.objects.all()
    if search_title:
        plants = plants.filter(
            Q(title__icontains=search_title) | Q(category__icontains=search_title)
        )

    return render(request, 'plants/search_plants.html', {
        'plants': plants,
        'search_title': search_title,
    })

'''
def search_countries(request):
    query = request.GET.get('query', '')
    countries = Country.objects.filter(name__icontains=query).values('id', 'name')[:10] 
    return JsonResponse(list(countries), safe=False)

'''