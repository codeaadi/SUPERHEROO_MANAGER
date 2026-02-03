
from django.urls import path
from . import views

urlpatterns = [
    path('',views.heroes, name='heroes'),
    path('branch/',views.hero_branch ,name ='herobranch'),
 
]