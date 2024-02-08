from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name ='mombai'
    dest1.dest = 'the city that never sleep'
    dest1.price = 600

    dest2 = Destination()
    dest2.name ='dubai'
    dest2.dest = 'grow crops niggas'
    dest2.price = 1000
    
    dest3 = Destination()
    dest3.name ='ukrian'
    dest3.dest = 'plant rice offten'
    dest3.price = 750
    dests = [dest1, dest2, dest3]
    return render(request, "index.html", {'dests':dests})