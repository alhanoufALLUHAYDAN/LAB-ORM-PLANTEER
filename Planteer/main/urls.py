from django.urls import path
from . import views 

app_name = "main"
urlpatterns = [
    path('', views.home_view, name='home_view'), 
    path('result/',views.search_results, name="search_results"),
    path('contact/', views.contact_view, name='contact_view'), 
    path('contact/messages/', views.messages_list_view, name='messages_list_view'),
    path('delete/<int:message_id>/', views.delete_message_view, name='delete_message'),
]
