from django.shortcuts import render, redirect , get_object_or_404
from django.core.paginator import Paginator
from .models import Plant, Country
from django.contrib import messages
from django.db.models import Q
from .forms import PlantForm
import random

def add_plant_view(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "The plant has been successfully added.")
            return redirect('plants:all_plants_view')  
    else:
        form = PlantForm()
    return render(request, 'plants/add_plant.html', {'form': form})

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
        messages.success(request, "Successfully deleted.")
        return redirect('plants:all_plants_view')  
    
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

def update_plant_view(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    print("Plant loaded for update:", plant.title, plant.about, plant.used_for) 
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated.")
            return redirect('plants:plant_detail_view', plant_id=plant.id)
    else:
        form = PlantForm(instance=plant)
    return render(request, 'plants/update_plant.html', {'form': form, 'plant': plant})
