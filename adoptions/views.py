from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Pet

def home(reuest):
    pets = Pet.objects.all()
    return render(reuest, 'home.html', {
        'pets': pets,
    })

def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('pet not found')
    return render(request, 'pet_details.html', {
        'pet': pet,
    })
