from django.shortcuts import render ,redirect , get_object_or_404
from django.http import HttpRequest
from plants.models import Plant
from .models import Contact
from .form import ContactForm
from django.contrib import messages


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


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been successfully sent. Please wait for a reply.")
            form = ContactForm()  
    else:
        form = ContactForm()
    return render(request, 'main/contact_us.html', {'form': form})

def messages_list_view(request):
    messages = Contact.objects.all().order_by('-created_at') 
    return render(request, 'main/messages.html', {'messages': messages})

def delete_message_view(request, message_id): 
    message = get_object_or_404(Contact, id=message_id) 
    if request.method == 'POST':
        message.delete() 
        return redirect('main:messages_list_view') 

    return render(request, 'main/delete_message.html', {'message': message})