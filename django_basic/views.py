from django.http import HttpResponse
from django.shortcuts import render




def home(request):
    # return HttpResponse('We are learning ')
    return render(request,'website/index.html')
def about(request):
 return render(request,'website/about.html')