from django.urls import path
from . import views 

app_name = "main"
urlpatterns = [
    path('', views.home_view, name='home_view'), 
    path('result/',views.search_results, name="search_results") ,
]
