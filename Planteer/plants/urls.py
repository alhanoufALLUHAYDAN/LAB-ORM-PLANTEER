from django.urls import path
from . import views 

app_name = "plants"
urlpatterns = [
    path('new/', views.add_plant_view, name='add_plant_view'), 
    path('all/', views.all_plants_view, name='all_plants_view'),
    path('<plant_id>/detail/', views.plant_detail_view, name='plant_detail_view'),
    #path('search_countries/', views.search_countries, name='search_countries'),
    path('<plant_id>/delete/', views.delete_plant_view, name='delete_plant_view'),  

]
