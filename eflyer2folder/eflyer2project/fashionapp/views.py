from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

# Create your views here.
def fabrics(request):
    return render(request, 'index.html', {'price':50})