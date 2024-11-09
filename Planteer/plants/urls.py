from django.urls import path
from . import views 
from django.shortcuts import render
from django.conf.urls import handler404

app_name = "plants"
urlpatterns = [
    path('new/', views.add_plant_view, name='add_plant_view'), 
    path('all/', views.all_plants_view, name='all_plants_view'),
    path('<plant_id>/detail/', views.plant_detail_view, name='plant_detail_view'),
    path('<plant_id>/delete/', views.delete_plant_view, name='delete_plant_view'), 
    path('<plant_id>/update/', views.update_plant_view, name='update_plant_view'),
    path('search/',views.search_plants_view, name='search_plants_view'),
]
handler404 = lambda request, exception: render(request, '404.html', status=404)
