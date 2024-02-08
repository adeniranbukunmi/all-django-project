from django.contrib import admin
from django.urls import path, include
from . import views as vw


urlpatterns =[
    path('eflyer2project/fashionapp', vw.fabrics, name="fabrics"),

]