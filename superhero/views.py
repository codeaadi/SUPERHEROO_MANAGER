from django.shortcuts import render
from .models import SuperHeroType

def heroes(request):
    heros= SuperHeroType.objects.all()
    return render(request,'superhero/heroes.html',{'heros':heros})

