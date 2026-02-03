from django.shortcuts import render
from .models import SuperHeroType,heroBranch

def heroes(request):
    heros= SuperHeroType.objects.all()
    return render(request,'superhero/heroes.html',{'heros':heros})

def hero_branch(request):
    branches =  heroBranch.objects.all()
    heroes = SuperHeroType.objects.all()
    return render(request,'hero_branch.html',{'branches':branches,'heroes':heroes})